import cv2
img=cv2.imread('wallpaper-night.jpg',1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite('wallpaper_copy.jpg',img)
