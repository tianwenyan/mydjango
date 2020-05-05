import cv2

# 读图 变为灰色
# img = cv2.imread('./code.png',cv2.IMREAD_GRAYSCALE)

# 写一张新图
# cv2.imwrite('./code.png',img)

from PIL import Image,ImageDraw

# 读图
# im = Image.open('./1.png')

# print(im.format,im.size,im.mode)

# 生成画笔
# draw = ImageDraw.Draw(im)

# 绘制
# draw.text((0,0),'1907',fill=(76,234,124,180),font=1,)
# im.show()

# 图片压缩
img = cv2.imread('./1.png')

# 压缩 0-9
# cv2.imwrite('./1.png',img,[cv2.IMWRITE_PNG_COMPRESSION],5)


# JPJ
cv2.imwrite('./PU.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,50])