import cv2
import argparse

def makeGray(image):
	image_len = len(image)
	for i in range(image_len):
		image_i_len = len(image[i])
		for j in range(image_i_len):
			if (image[i][j]>[160,160,160]).all():
				continue
			else:
				image[i][j] = [0, 0, 0]


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num", type=str, required=True,
	help="path to input image where we'll apply template matching")
args = vars(ap.parse_args())

#read file
num = args['num']
numCV2 =  cv2.imread(f'number/blood/{num}.jpg')


#change color
makeGray(numCV2)

#show image
cv2.imshow("After NMS", numCV2)
key = cv2.waitKey(0)

#judge whether save
if key == 13:
    cv2.imwrite(f'number/blood/{num}.jpg',numCV2)

#python tool/toBlackAndWhite.py -n 5
