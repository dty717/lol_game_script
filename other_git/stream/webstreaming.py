# import the necessary packages
from webcamvideostream import WebcamVideoStream
from pyimagesearch.motion_detection import SingleMotionDetector
from flask import Response
from flask import Flask
from flask import render_template
import threading
import argparse
import datetime
import champ_list
import globby
import time
import cv2 as cv

current_champion = ''
current_confidence = 0.85
globby.init()

def calculate_spot(x, y):
    # print(x,y)
  return
  # if x < y and x < (350 - y):
    #     audio_player.play('top-left')
    # elif x < y and x > (350 - y):
    #     audio_player.play('bottom-left')
    # elif x > y and x > (350 - y):
    #     audio_player.play('bottom-right')
    # elif x > y and x < (350 - y):
    #     audio_player.play('top-right')


def change_champion():
    setting = champ_list.get_champion(globby.champion_name)
    image = setting.image

    cvChamp = cv.imread(f'champions/{image}.png')
    cvChamp = cv.resize(cvChamp, (28, 28), interpolation=cv.INTER_AREA)
    cvChamp = cvChamp[5:23, 5:23]
    global current_champion
    current_champion = globby.champion_name

    global current_confidence
    current_confidence = (setting.confidence)
    globby.set_confidence(current_confidence)

    return (cvChamp, setting)



def on_confidence_updated(c):
    global current_confidence
    current_confidence = c


def on_ui_save(confidence):
    champ_list.save_setting(current_champion, confidence)



# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful when multiple browsers/tabs
# are viewing the stream)
outputFrame = None
lock = threading.Lock()
# initialize a flask object
app = Flask(__name__)
# initialize the video stream and allow the camera sensor to
# warmup
#vs = VideoStream(usePiCamera=1).start()
vs = WebcamVideoStream(src=1).start()
time.sleep(2.0)

@app.route("/")
def index():
  # return the rendered template
  return render_template("index.html")

countWhite = 45
def getWhite(mm):
  mm_len = len(mm)
  global countWhite
  for i in range(mm_len):
    _i = mm_len - i - 1
    mm_i_len = len(mm[_i])
    _countWhite = 0
    for j in range(mm_i_len):
      if (mm[_i][j]>[200,200,200]).all():
        _countWhite += 1
        if _countWhite>countWhite:
          print(_i)
          break
      else:
        _countWhite =0
# >>> countWhite = 45
# >>> getWhite(img)
# 149
# 113
# 112


def detect_motion(frameCount):
  # grab global references to the video stream, output frame, and
  # lock variables
  global vs, outputFrame, lock
  # initialize the motion detector and the total number of frames
  # read thus far
  md = SingleMotionDetector.SingleMotionDetector(accumWeight=0.1)
  global current_champion
  current_champion = globby.champion_name

  global current_confidence
  current_confidence = globby.confidence

  (cvChamp, setting) = change_champion()

  globby.sub_confidence(on_confidence_updated)
  
  # loop over frames from the video stream
  while True:
    # read the next frame from the video stream, resize it,
    # convert the frame to grayscale, and blur it
    if current_champion != globby.champion_name:
      (cvChamp, setting) = change_champion()
    # print(current_champion)
    w = 1920
    h = 1080

    if cv.waitKey(20) & 0xFF == ord('d'):
      break

    if globby.closing:
      break

    # img = ImageGrab.grab(bbox=(w-350, h-390, w, h))  # x, y, w, h
    img = vs.read()
    # print(len(img),len(img[0]))
    img =img[h-306:h-40, w-265: w]  # x, y, w, h
    mm = img

    # img_np = np.array(img)
    # mm = cv.cvtColor(img_np, cv.COLOR_RGBA2BGR)

    result = cv.matchTemplate(cvChamp, mm, cv.TM_SQDIFF_NORMED)
    mn, _, mnLoc, _ = cv.minMaxLoc(result)
    confidence = 1-mn

    rect_color = (0, 255, 0)
    if confidence > current_confidence:
      MPx, MPy = mnLoc
      trows, tcols = cvChamp.shape[:2]
      # print((MPx, MPy), MPy - MPx)
      calculate_spot(MPx, MPy)
      cv.rectangle(mm, (MPx, MPy), (MPx+tcols, MPy+trows), rect_color, 2)

    # rgb_mm = cv.cvtColor(mm, cv.COLOR_BGR2RGBA)
    # pilImg = Image.fromarray(rgb_mm)

    # globby.image = pilImg

    # frame = imutils.resize(frame, width=400)
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # gray = cv.GaussianBlur(gray, (7, 7), 0)
    # # grab the current timestamp and draw it on the frame
    # timestamp = datetime.datetime.now()
    # cv.putText(frame, timestamp.strftime(
    #   "%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
    #   cv.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    # # if the total number of frames has reached a sufficient
    # # number to construct a reasonable background model, then
    # # continue to process the frame
    # if total > frameCount:
    #   # detect motion in the image
    #   motion = md.detect(gray)
    #   # check to see if motion was found in the frame
    #   if motion is not None:
    #     # unpack the tuple and draw the box surrounding the
    #     # "motion area" on the output frame
    #     (thresh, (minX, minY, maxX, maxY)) = motion
    #     cv.rectangle(frame, (minX, minY), (maxX, maxY),
    #       (0, 0, 255), 2)
    
    # # update the background model and increment the total number
    # # of frames read thus far
    # md.update(gray)
    # total += 1
    # acquire the lock, set the output frame, and release the
    # lock
    with lock:
      outputFrame = mm.copy()

def generate():
  # grab global references to the output frame and lock variables
  global outputFrame, lock
  # loop over frames from the output stream
  frameTimes = 2000
  while frameTimes>0:
    frameTimes-=1
    # wait until the lock is acquired
    with lock:
      # check if the output frame is available, otherwise skip
      # the iteration of the loop
      if outputFrame is None:
        continue
      # encode the frame in JPEG format
      (flag, encodedImage) = cv.imencode(".jpg", outputFrame)
      # ensure the frame was successfully encoded
      if not flag:
        continue
    # yield the output frame in the byte format
    yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
      bytearray(encodedImage) + b'\r\n')

@app.route("/video_feed")
def video_feed():
  # return the response generated along with the specific media
  # type (mime type)
  return Response(generate(),
    mimetype = "multipart/x-mixed-replace; boundary=frame")

# check to see if this is the main thread of execution
if __name__ == '__main__':
  # construct the argument parser and parse command line arguments
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--ip", type=str, required=True,
    help="ip address of the device")
  ap.add_argument("-o", "--port", type=int, required=True,
    help="ephemeral port number of the server (1024 to 65535)")
  ap.add_argument("-f", "--frame-count", type=int, default=32,
    help="# of frames used to construct the background model")
  args = vars(ap.parse_args())
  # start a thread that will perform motion detection
  t = threading.Thread(target=detect_motion, args=(
    args["frame_count"],))
  t.daemon = True
  t.start()
  # start the flask app
  app.run(host=args["ip"], port=args["port"], debug=True,
    threaded=True, use_reloader=False)
# release the video stream pointer
vs.stop()

