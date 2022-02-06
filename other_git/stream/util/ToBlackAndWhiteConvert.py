#api
def makeGray(image):
  image_len = len(image)
  for i in range(image_len):
    image_i_len = len(image[i])
    for j in range(image_i_len):
      if (image[i][j]>[160,160,160]).all():
        continue
      else:
        image[i][j] = [0, 0, 0]

