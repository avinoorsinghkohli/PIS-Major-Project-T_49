import cv2
import numpy as np
from scipy.stats import itemfreq
def signboard(image, n_colors):
    pixels = np.float32(image).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    flags, labels, centroids = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    p = np.uint8(centroids)
    return p[np.argmax(itemfreq(labels)[:, -1])]
cameraCapture = cv2.VideoCapture(0) 
cv2.namedWindow('ORVM Mounted Camera')
s,f = cameraCapture.read()
while s==True:
    cv2.waitKey(1)
    s, f = cameraCapture.read()

    gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray, 37)
    c = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,1, 50, param1=120, param2=40)
    if(c is not None):
        c = np.uint16(np.around(c))
        max_r, max_i = 0, 0
        for i in range(len(c[:, :, 2][0])):
            if c[:, :, 2][0][i] > 50 and c[:, :, 2][0][i] > max_r:
                max_i = i
                max_r = c[:, :, 2][0][i]
        x, y, r = c[:, :, :][0][max_i]
        if y > r and x > r:
            square = f[y-r:y+r, x-r:x+r]

            dominant_color = signboard(square, 2)
            if dominant_color[2] > 50:
                print("Slow Down!")                    
            else:
                print("GO!!")
        

        for i in c[0, :]:
            cv2.circle(f, (i[0], i[1]), i[2], (0, 255, 233), 5)
            cv2.circle(f, (i[0], i[1]), 2, (34, 0, 255), 3)
    cv2.imshow('ORVM Mounted Camera', f)


cv2.destroyAllWindows()
cameraCapture.release()
