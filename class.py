import cv2
import numpy as np

img=cv2.imread("lena.png")

scr2=255*np.ones((img.shape[0],img.shape[1],3),dtype=np.uint8)

cv2.line(scr2,(50,0),(50,img.shape[1]),(0,255,0),13) 
cv2.line(scr2,(100,0),(100,img.shape[1]),(255,0,0),13)
cv2.line(scr2,(150,0),(150,img.shape[1]),(0,0,255),13)

blend=cv2.addWeighted(img,0.7,scr2,0.3,0)

cv2.imwrite("line.png",blend)
import cv2
import numpy as np

img=cv2.imread("lena.png")

scr2=img.copy()

cv2.line(scr2,(50,0),(50,img.shape[1]),(0,255,0),13) 
cv2.line(scr2,(100,0),(100,img.shape[1]),(255,0,0),13)
cv2.line(scr2,(150,0),(150,img.shape[1]),(0,0,255),13)

blend=cv2.addWeighted(img,0.7,scr2,0.3,0)

cv2.imwrite("line.png",blend)

