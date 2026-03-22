import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. 读取图片
img = cv2.imread('test.jpg.png')

# 2. 输出图像信息
height, width, channels = img.shape
print(f"图像尺寸：宽度={width}, 高度={height}")
print(f"通道数：{channels}")
print(f"数据类型：{img.dtype}")

# 3. 显示原图
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('原图')
plt.axis('off')

# 4. 转灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 显示灰度图
plt.subplot(1,2,2)
plt.imshow(gray, cmap='gray')
plt.title('灰度图')
plt.axis('off')

plt.show()

# 5. 保存灰度图
cv2.imwrite('gray_image.jpg', gray)
print("已保存 gray_image.jpg")

# 6. 裁剪左上角100x100并保存
crop = img[0:100, 0:100]
cv2.imwrite('cropped.jpg', crop)
print("已保存 cropped.jpg")

print("实验完成！")