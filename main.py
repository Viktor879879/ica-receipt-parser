import cv2
import matplotlib.pyplot as plt
import easyocr

reader = easyocr.Reader(['sv', 'en'])
result = reader.readtext('data/raw/kvitto6.jpeg')
print(result)

for bbox, text, conf in result:
    print(text)

new_three_in_row = []
for bbox, text, conf in result:
    new_three_in_row.append((bbox[0][1], bbox[0][0], text))


sorted_list = sorted(new_three_in_row)
for pars in sorted_list:
    print(pars)

current_line = []
prev_y = 0

for y, x, text in sorted_list:
    if y - prev_y > 10:
        sorted_ = sorted(current_line)
        texts = [t for _, t in sorted_]
        new_line = ' '.join(texts)
        print(new_line)
        current_line = []
        current_line.append((x, text))
    elif y - prev_y < 10:
        current_line.append((x, text))
    prev_y = y

new = sorted(current_line)
word = [t for _, t in new]
new_line1 = ' '.join(word)
print(new_line1)


img6 = cv2.imread('data/raw/kvitto6.jpeg')
img6 = cv2.cvtColor(img6, cv2.COLOR_BGR2RGB)

img6_v2 = cv2.imread('data/raw/kvitto6.jpeg', cv2.IMREAD_GRAYSCALE)

print(img6.shape[0])
print(img6.shape)
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
# plt.show()