#!/usr/bin/python3

import  cv2

#  detecting  webcame
#  here arg means camera number -- two internal web , external web 
#  selecting  camera first 
cap=cv2.VideoCapture(0)

# checking  for camera status 

while  cap.isOpened() :
    #  start taking pictures 
    status,frame=cap.read()
    bwimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('current',frame)
    cv2.imshow('oldjamane',bwimg)
    if cv2.waitKey(30) & 0xFF == ord('q') :
        break


cv2.destroyAllWindows()
cap.release()



