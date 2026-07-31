import cv2
import matplotlib.pyplot as plt

img6 = cv2.imread('data/raw/kvitto6.jpeg')
img6 = cv2.cvtColor(img6, cv2.COLOR_BGR2RGB)

img6_v2 = cv2.imread('data/raw/kvitto6.jpeg', cv2.IMREAD_GRAYSCALE)

binary_global = (img6_v2 > 127) * 255
binary_adaptive = cv2.adaptiveThreshold(
    img6_v2, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    23, 14
)

plt.subplot(1, 2, 1)
plt.imshow(binary_global, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(binary_adaptive, cmap="gray")
plt.show()