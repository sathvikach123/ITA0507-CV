import cv2

img = cv2.imread(r"C:\Users\SATHVIKA\OneDrive\Desktop\cv.jpeg")
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Rotated Image", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
