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
    cv2.rectangle(frame,(50,50),(300,300),(0,0,255),3)
    cv2.imshow('current',frame)
    if cv2.waitKey(30) & 0xFF == ord('q') :
        break


cv2.destroyAllWindows()
cap.release()



