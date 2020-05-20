import cv2
import numpy as np
 
# Load the image in greyscale
img = cv2.imread('small.jpg',0)
 
# Apply Gaussian Blur
blur = cv2.GaussianBlur(img,(3,3),0)
 
# Apply Laplacian operator in some higher datatype
laplacian = cv2.Laplacian(blur,cv2.CV_64F)

laplacian1 = laplacian/laplacian.max()
 
cv2.imshow('a7',laplacian1)
cv2.waitKey(0)

"""
for i in range(0, len(images_List)):
  fileName = images_List[i]
  image = Normalise(np.array(cv2.imread("/home/nitigyapant/Desktop/Books/college/Third Year/Winter semester/MCA" + fileName, 0)))
  image = cv2.resize(image, (512, 512))
  k = 1.5
  sigma = 1
  fileName = fileName.split(".")[0]
  feature_Space1 = Blob_changing_Sigma(image, sigma, k, 10)
  feature_Space2 = Non_maxima_Supr(feature_Space1, 0.01, image)
  # print(np.array(feature_Space2).shape)
  # print(feature_Space2[1])
  np.savetxt("/home/nitigyapant/Desktop/Books/college/Third Year/Winter semester/MCA" + fileName + ".txt", feature_Space2)
  if(i%300 == 0):
    print(i, len(feature_Space2))

"""
