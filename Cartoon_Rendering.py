import cv2
import numpy as np

def color_quantization(img, k=8):
    data = np.float32(img).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
    _, labels, centers = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    result = centers[labels.flatten()]
    result = result.reshape(img.shape)
    return result

img = cv2.imread('Cat.jpeg')  

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges_canny = cv2.Canny(gray, threshold1=200, threshold2=200)

edges_inv = cv2.bitwise_not(edges_canny)

kernel = np.ones((5, 5), np.uint8)
edges_dilated = cv2.dilate(edges_inv, kernel, iterations=2)

edges_colored = cv2.cvtColor(edges_dilated, cv2.COLOR_GRAY2BGR)

quantized = color_quantization(img, k=8)
blurred = cv2.bilateralFilter(quantized, d=9, sigmaColor=300, sigmaSpace=300)

cartoon = cv2.bitwise_and(blurred, edges_colored)

cv2.imshow("Original", img)
cv2.imshow("Cartoon", cartoon)
print("ESC 키를 누르면 창이 닫힙니다.")

while True:
    key = cv2.waitKey(0)
    if key == 27:
        break

cv2.destroyAllWindows()
cv2.waitKey(0)