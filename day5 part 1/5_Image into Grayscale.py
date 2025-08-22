import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpeg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(cv2.cvtColor(gray,cv2.COLOR_BGR2RGB))
plt.show()