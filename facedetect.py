#!/usr/bin/env python3

# importing opencv module 
import  cv2
#  reading an image 
img=cv2.imread('celeb.jpg')
print(img.shape)
# reading frontface cascade file
faced=cv2.CascadeClassifier('haarface.xml')
# loading xml file have number of functions
print(dir(faced))

while True:
    grayhuman=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #get_face=faced.detectMultiScale(grayhuman,1.15,5)
    get_face=faced.detectMultiScale(img,1.15,5)

    for  (x,y,w,h) in  get_face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
        imgface_roi=grayhuman[y:y+h,x:x+w]


    cv2.imshow('grayimg',img)

    if cv2.waitKey(0) & 0xFF  ==  ord('q'):
        break

cv2.destroyAllWindows()







