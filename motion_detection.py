#!/usr/bin/python3

import  cv2

# defining function for image diff
def  img_diff_create(x,y,z):
    img_diff1=cv2.absdiff(x,y)
    img_diff2=cv2.absdiff(y,z)
    img3=cv2.bitwise_and(img_diff1,img_diff2)
    return img3


#  starting  camera
cap=cv2.VideoCapture(0)
# taking first frame 
take1=cap.read()[1]
take2=cap.read()[1]
take3=cap.read()[1]

# converting to grayscale 
gray1=cv2.cvtColor(take1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(take2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(take3,cv2.COLOR_BGR2GRAY)

while True:
    # calling  function to use gray scaled image 
    new_img=img_diff_create(gray1,gray2,gray3)
    cv2.imshow('dfff',new_img)
    # reading more  images
    status,frame=cap.read()
    # showing  original image
    #cv2.imshow('original',frame)
    # image transpose operation 
    gray1=gray2
    gray2=gray3
    gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if cv2.waitKey(30) & 0xFF == ord('q') :
        break


cv2.destroyAllWindows()
cap.release()


