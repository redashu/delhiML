#!/usr/bin/python3

import  cv2
#  selecting  camera first 
cap=cv2.VideoCapture(0)

#  getting  frame size  width , heigh 
w=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(w)
print(h)
#  defining video format 
v_format=cv2.VideoWriter_fourcc(*'XVID')
#  saving  video as per frame speed         FPS  , 
v_out=cv2.VideoWriter('/tmp/classml.avi',v_format,25.0,(int(w),int(h)))
# checking  for camera status 

while  cap.isOpened() :
    #  start taking pictures 
    status,frame=cap.read()
    cv2.imshow('current',frame)
    v_out.write(frame)
    
    if cv2.waitKey(30) & 0xFF == ord('q') :
        break


cv2.destroyAllWindows()
cap.release()



