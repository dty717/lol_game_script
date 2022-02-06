import cv2
import argparse
import numpy as np
from util.ToBlackAndWhiteConvert import makeGray

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image where we'll apply template matching")
ap.add_argument("-b", "--threshold", type=float, default=0.8,
	help="threshold for multi-template matching")
args = vars(ap.parse_args())

#init
nums = 10
cvChampList = []
for num in range(nums):
	cvChampList.append(cv2.imread(f'number/qwer/{num}.jpg'))

#read file
image = args['image']
imageCV2 =  cv2.imread(f'images/g0/{image}')

line = [738,792,  800,854, 862,915, 923,977]
lineLen = len(line)
for i in range(lineLen):
	_i = lineLen - i - 1
	line[_i] = line[_i] - line[0]
#draw rect
# cv2.rectangle(imageCV2, (738, 892), (977, 918),
# 		(255, 0, 0), 1)
# cv2.imshow("After NMS", imageCV2)

_image = imageCV2[892:918,738:977].copy()

makeGray(_image)
qWaitTimeList = []
wWaitTimeList = []
eWaitTimeList = []
rWaitTimeList = []

for num in range(nums):
	result = cv2.matchTemplate(_image, cvChampList[num],
		cv2.TM_CCOEFF_NORMED)
	(yCoords, xCoords) = np.where(result >= args["threshold"])
	# clone = _image.copy()
	# print("[INFO] {} matched locations *before* NMS".format(len(yCoords)))
	# loop over our starting (x, y)-coordinates
	lastX = 0
	for (x, y) in zip(xCoords, yCoords):
		# draw the bounding box on the image
		if x - lastX < 5:
			continue
		else:
			lastX = x
		if x>line[0] and x<line[1]:
			qWaitTimeList.append(num)
		elif x>line[2] and x<line[3]:
			wWaitTimeList.append(num)
		elif x>line[4] and x<line[5]:
			eWaitTimeList.append(num)
		elif x>line[6] and x<line[7]:
			rWaitTimeList.append(num)
		else:
			print(x)
		# cv2.rectangle(clone, (x, y), (x + 10, y + 20),
		# 	(255, 0, 0), 1)
	# show our output image *before* applying non-maxima suppression
	# cv2.imshow("Before NMS", clone)
# print(qWaitTimeList,wWaitTimeList,eWaitTimeList,rWaitTimeList)

def waitTime(waitTimeList):
	waitTime = 0
	if waitTimeList:
		waitTimeListLen = len(waitTimeList)
		if waitTimeList[0]==0:
			if waitTimeListLen == 2:
				waitTime = waitTimeList[1]/10
		else:
			for i in range(waitTimeListLen):
				waitTime = waitTime*10+waitTimeList[i]
	return waitTime


qWaitTime = waitTime(qWaitTimeList)
wWaitTime = waitTime(wWaitTimeList)
eWaitTime = waitTime(eWaitTimeList)
rWaitTime = waitTime(rWaitTimeList)
# print(qWaitTime,wWaitTime,eWaitTime,rWaitTime)
#show image
# cv2.imshow("After NMS", _image)
# key = cv2.waitKey(0)


#blood
_image = imageCV2[954:969,792:978].copy()
# _image = imageCV2[972:988,792:978].copy()

makeGray(_image)
height_image = len(_image)
width_image = len(_image[0])
for i in range(width_image):
	if (_image[height_image-1][i]>(160,160,160)).all():
		for j in range(height_image):
			_image[j][i] = (0,0,0)
# cv2.imwrite(f'test_{image}.jpg',_image)
# cv2.imshow("After NMS", _image)
# key = cv2.waitKey(0)

nums = 10
cvBloodChampList = []
slashPos = 0
for num in range(nums):
	cvBloodChampList.append(cv2.imread(f'number/blood/{num}.jpg'))

cvBloodChampList.append(cv2.imread(f'number/blood/slash.jpg'))
slashResult = cv2.matchTemplate(_image, cvBloodChampList[nums], cv2.TM_SQDIFF_NORMED)
mn, _, mnLoc, _ = cv2.minMaxLoc(slashResult)
slashConfidence = 1-mn
# print(mn,mnLoc)
if slashConfidence>args["threshold"]:
	slashPos = mnLoc[0]

currentBloodList = []
maxBloodList = []
def suitableList(list,item):#item=(num,x,possibility)
	listLen = len(list)
	(_num,_x,_possibility) = item
	global slashPos
	if _x < slashPos + 2 and _x> slashPos-2:
		return
	for i in range(listLen):
		listX = list[i][1]
		if _x < listX+4 and _x > listX-4:
			listPossibility =list[i][2]
			if _possibility > listPossibility:
				list[i] = item
			return
		elif _x < listX:
			list.insert(i, item)
			return
	list.append(item)

def suitableListValue(list):#list=[(num,x,possibility)]
	listLen = len(list)
	value = 0
	for i in range(listLen):
		listNum = list[i][0]
		value = 10*value + listNum
	return value

if slashPos > 0:
	for num in range(nums):
		result = cv2.matchTemplate(_image, cvBloodChampList[num],
			cv2.TM_CCOEFF_NORMED)
		(yCoords, xCoords) = np.where(result >= args["threshold"])
		# clone = _image.copy()
		# loop over our starting (x, y)-coordinates
		lastX = 0
		for (x, y) in zip(xCoords, yCoords):
			# draw the bounding box on the image
			if x>slashPos:
				suitableList(maxBloodList,(num,x,max(result[0][x],result[1][x])))
			else:
				suitableList(currentBloodList,(num,x,max(result[0][x],result[1][x])))
			# cv2.rectangle(clone, (x, y), (x + 10, y + 20),
	currentBlood = suitableListValue(currentBloodList)
	maxBlood = suitableListValue(maxBloodList)
	print(currentBlood,maxBlood)
	cv2.imshow("After NMS", _image)
	key = cv2.waitKey(0)


#judge whether save
# if key == 13:
#     cv2.imwrite(f'time/{image}.jpg',imageCV2)

#python QWER_Time.py -i EjforLrXh7.jpg --threshold 0.85