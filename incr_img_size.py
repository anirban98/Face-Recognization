import cv2

img = cv2.imread ("C:\\Users\\Tanishi\\Desktop\\panda.jpg",0);

resized = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)));

cv2.imshow("pandas",img)
cv2.waitKey(1000)

cv2.destroyAllWindows()
