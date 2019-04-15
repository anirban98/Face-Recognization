import cv2

img = cv2.imread ("C:\\Users\\Tanishi\\Desktop\\panda.jpg",0);
print(img.shape);

cv2.imshow("pandas",img)
cv2.waitKey(0)
