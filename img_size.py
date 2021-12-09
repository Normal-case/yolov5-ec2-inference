import cv2

src = cv2.imread('test.jpg')
src = cv2.resize(src, dsize=(1280, 1280))

cv2.imwrite('resize.jpg', src)