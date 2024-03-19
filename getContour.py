import cv2
import numpy as np





def getContours(img):
    imgContour = img.copy()
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    # imgContour = np.zeros_like(img)
    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)
    return biggest
