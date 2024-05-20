import cv2
img=cv2.imread("image.jpg")
print(img)
gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gry)
cv2.imwrite("image.jpg",gry)