#!/usr/bin/env python3

# importing opencv module 
import  cv2
#  reading an image 
img=cv2.imread('catdog2.jpg',1)
# 1 means exam same color 
img1=cv2.imread('catdog2.jpg',0)
# unchange color maintain image transparancy 
img2=cv2.imread('catdog2.jpg',-1)

# 0 means  black & white -- grayscale image
'''
imgread----  3  parameter

i)  colored
ii)  grayscale with black & white
iii)  unchange color ---

'''
# print original data 
print(img)
# checking shape 
print(img.shape)

# now showing that image 
cv2.imshow('window1',img)
cv2.imshow('window2',img1)
cv2.imshow('window3',img2)

# only saving  grayscale image
cv2.imwrite('/home/code/Desktop/class2.jpg',img1)
# to hold above window for unlimited time 
cv2.waitKey(0)
#  destroy particular window
#cv2.destroyWindow('window1')
#cv2.destroyWindow('window2')
cv2.destroyAllWindows()






