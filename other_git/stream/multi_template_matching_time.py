# import the necessary pages
from imutils.object_detection import non_max_suppression
import numpy as np
import argparse
import cv2
import pytesseract
from util.ToBlackAndWhiteConvert import makeGray

heroes = ["Veigar","Kayle","Orianna","Volibear","Teemo","Corki","LeBlanc","Swain","Karthus","Quinn","Home"]
heroesLen = len(heroes)
cvChampList = []
for hero in heroes:
	cvChampList.append(cv2.imread(f'name_label/{hero}_name.jpg'))


def getResults(mm):
	global cvChampList,heroesLen
	for cvChampIndex in range(heroesLen):
		cvChamp = cvChampList[cvChampIndex]
		result = cv2.matchTemplate(cvChamp, mm, cv2.TM_SQDIFF_NORMED)
		mn, _, mnLoc, _ = cv2.minMaxLoc(result)
		confidence = 1-mn
		if confidence>args["threshold"]:
			return heroes[cvChampIndex]
	return None

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image where we'll apply template matching")
ap.add_argument("-t", "--template", type=str, required=True,
	help="path to template image")
ap.add_argument("-b", "--threshold", type=float, default=0.8,
	help="threshold for multi-template matching")
args = vars(ap.parse_args())

# load the input image and template image from disk, then grab the
# template image spatial dimensions
print("[INFO] loading images...")
image = cv2.imread(args["image"])
template = cv2.imread(args["template"])
(tH, tW) = template.shape[:2]
# display the  image and template to our screen
cv2.imshow("Image", image)
cv2.imshow("Template", template)

# convert both the image and template to grayscale
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
# perform template matching
print("[INFO] performing template matching...")
result = cv2.matchTemplate(imageGray, templateGray,
	cv2.TM_CCOEFF_NORMED)

# find all locations in the result map where the matched value is
# greater than the threshold, then clone our original image so we
# can draw on it
(yCoords, xCoords) = np.where(result >= args["threshold"])
clone = image.copy()
print("[INFO] {} matched locations *before* NMS".format(len(yCoords)))
# loop over our starting (x, y)-coordinates
for (x, y) in zip(xCoords, yCoords):
	# draw the bounding box on the image
	cv2.rectangle(clone, (x, y), (x + tW, y + tH),
		(255, 0, 0), 3)
# show our output image *before* applying non-maxima suppression
cv2.imshow("Before NMS", clone)
# cv2.waitKey(0)

# initialize our list of rectangles
rects = []
# loop over the starting (x, y)-coordinates again
for (x, y) in zip(xCoords, yCoords):
	# update our list of rectangles
	rects.append((x, y, x + tW, y + tH))
# apply non-maxima suppression to the rectangles
pick = non_max_suppression(np.array(rects))
print("[INFO] {} matched locations *after* NMS".format(len(pick)))
# loop over the final bounding boxes
for (startX, startY, endX, endY) in pick:
	# draw the bounding box on the image
	centerColor = image[int((startY+endY)/2),int((startX+endX)/2)]
	if 'friend' in args["template"]:
		if centerColor[0] > 30 and centerColor[1] > 20 and centerColor[2] < 10:
			pass
		else:
			continue
	elif 'enemy' in args["template"]:
		if centerColor[0] < 10 and centerColor[1] < 10 and centerColor[2] > 30:
			pass
		else:
			continue
	if startY-35 < 0: startY=35
	if endY-28 < 0: endY=28
	_image = image[startY-35:endY-28,startX+25:endX+85].copy()
	makeGray(_image)
	heroName = getResults(_image)
	if heroName:
		cv2.imwrite(heroName+str(startX)+".jpg", _image)
	else:
		cv2.imwrite('heroName'+str(startX)+".jpg", _image)
	cv2.rectangle(image, (startX+25, startY-35), (endX+85, endY-28),
		(255, 0, 0), 1)

# show the output image
cv2.imshow("After NMS", image)
cv2.waitKey(0)


# python multi_template_matching_time.py --image images/g0/GCy9McHOAE.jpg --template images/enemy.jpg --threshold 0.92