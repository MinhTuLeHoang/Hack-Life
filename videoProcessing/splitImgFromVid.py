import os
import cv2

videoPath = '/Users/lap15864-local/Documents/Zalo Received Files/mix_traffic_signv2.avi'

print("file exists?", os.path.exists(videoPath))

vid = cv2.VideoCapture(videoPath)
currentframe = 0

while(True):
    ret, frame = vid.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    if ret:
        cv2.imshow("name", frame)
        cv2.imwrite("/Users/lap15864-local/temp/Hack-Life/outputs/pics/f" + str(currentframe) + ".png", frame)
        currentframe += 1
    else:
        break
vid.release()
cv2.destroyAllWindows()
