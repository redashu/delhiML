#!/usr/bin/env python3

# importing opencv module 
import  cv2
#  reading an image 
img=cv2.imread('dogs.jpg')

# print  resolution of image
print(img.shape)
# draw a line 
#   image data , starting co-ordinate , end co-ordinate , color , width of line
cv2.line(img,(0,0),(190,240),(0,0,255),10)
#  rectangle 
cv2.rectangle(img,(190,240),(300,100),(120,20,200),2)


# showing image
cv2.imshow('www',img)
cv2.waitKey(0)
cv2.destroyAllWindows()





