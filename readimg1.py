import cv2
img = cv2.imread("gg.jpg")

cv2.putText (img,
                "Sun",
                (100, 80), cv2.FONT_HERSHEY_COMPLEX,
                2,
                (255,0,0)),

cv2.putText (img,
                "Mercury",
                (110, 180), cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,0))

cv2.putText (img,
                "Venus",
                (190, 270), cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,0))

cv2.putText (img,
                "Earth",
                (300, 270), cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,0))
cv2.putText (img,
                "Mars",
                (400, 90), cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,0))
cv2.putText (img,
                "Jupiter",
                (500, 110), cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,0))
cv2.putText (img,
                "Saturn",
                (750, 130), cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,0))
cv2.putText (img,
                "Uranus",
                (950, 130), cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,0))
cv2.putText (img,
                "Neptune",
                (1000, 80), cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,0))
cv2.imshow("Solar Sysytem", img)
cv2.waitKey(0)
cv2.imwrite("newgg.jpg",img)

