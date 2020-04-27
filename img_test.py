import cv2

# 读图 变为灰色
img = cv2.imread('./code.png',cv2.IMREAD_GRAYSCALE)

# 写一张新图
cv2.imwrite('./code.png',img)