import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpeg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
edges = cv2.Canny(gray,50,100)
plt.imshow(cv2.cvtColor(edges,cv2.COLOR_BGR2RGB))
plt.show()