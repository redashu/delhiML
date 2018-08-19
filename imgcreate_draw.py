#!/usr/bin/env python3

# importing opencv module 
import  cv2
import  numpy    as  np
#  reading an image 
img=np.zeros((512,512,3))
#img=np.full((512,512,3),255)
#img=cv2.imread('dogs.jpg')

# print  resolution of image
print(img.shape)
# draw a line 
#   image data , starting co-ordinate , end co-ordinate , color , width of line
cv2.line(img,(0,0),(190,240),(0,0,255),10)
#  rectangle 
cv2.rectangle(img,(190,240),(300,100),(120,20,200),4)
font=cv2.FONT_HERSHEY_SIMPLEX
#                       starting point , font size , font width
cv2.putText(img,'dogs',(300,100),font,2,(255,255,0),3,cv2.LINE_AA)

#  drawing  circle 
#                center,radius , color ,  width
cv2.circle(img,(150,250),100,(123,200,160),3)

# showing image
cv2.imshow('www',img)
cv2.waitKey(0)
cv2.destroyAllWindows()





