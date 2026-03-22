import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. 读入图像
img = cv2.imread('test.jpg')

# 2. 获取 RGB 数值（选择图像中心点的像素）
height, width, channels = img.shape
center_y, center_x = height // 2, width // 2
pixel_bgr = img[center_y, center_x]  # OpenCV 默认是 BGR 顺序
print(f"图像中心点 ({center_x}, {center_y}) 的像素值 (B,G,R): {pixel_bgr}")
print(f"RGB 数值 (R,G,B): ({pixel_bgr[2]}, {pixel_bgr[1]}, {pixel_bgr[0]})")

# 3. 转换到 YCrCb 色彩空间（OpenCV 用的是 YCrCb，不是 YCbCr）
# 注意：OpenCV 中 cvtColor 使用 COLOR_BGR2YCrCb
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# 分离三个通道
Y, Cr, Cb = cv2.split(ycrcb)

# 4. 分别显示三个通道
plt.figure(figsize=(15, 4))

plt.subplot(1, 4, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(Y, cmap='gray')
plt.title('Y Channel (Luminance)')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(Cr, cmap='gray')
plt.title('Cr Channel (Red difference)')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(Cb, cmap='gray')
plt.title('Cb Channel (Blue difference)')
plt.axis('off')

plt.tight_layout()
plt.show()

# 额外：输出每个通道的数值范围
print(f"\nY 通道范围: {Y.min()} - {Y.max()}")
print(f"Cr 通道范围: {Cr.min()} - {Cr.max()}")
print(f"Cb 通道范围: {Cb.min()} - {Cb.max()}")

print("\n练习题完成！")