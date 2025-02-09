import random
import cv2
import numpy as np

pathOutput = "E:/DatasetContainer/AI_container/realData/dataset/"
checkedList = []

def mousePoints(event,x,y,flags,params):
      global counter
      # Left button click
      if event == cv2.EVENT_LBUTTONDOWN:
        polyPoint.append([x,y])

frameList = []

for i in range(1,11):
  pathTest = "E:/DatasetContainer/AI_container/realData/video"+str(i)+".MOV"
  tmp = 10
  if i==1:
    tmp = 20
  cap = cv2.VideoCapture(pathTest)
  videoLength = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
  for j in range(videoLength//tmp - tmp):
    checkedList.append("n")
    cap.set(cv2.CAP_PROP_POS_FRAMES, j*tmp)
    ret, frame = cap.read()
    frameList.append(frame)
  cap.release()
  print("video",i,"done")


polyPoint = []

print("-> ",len(checkedList))


while True:
  counter = int(random.random()*len(checkedList))
  while checkedList[counter] == "y":
    counter = int(random.random()*len(checkedList))
  frame = cv2.resize(frameList[counter],(512,512))
  cv2.imshow('Frame',frame)
  cv2.setMouseCallback("Frame", mousePoints)

  # Display the resulting frame
  frame = cv2.resize(frame,(512,512))
  blankImg = np.zeros((212,512,3),dtype = "uint8")
  frame2 = cv2.vconcat([frame,blankImg])
  cv2.imshow('Frame',frame2)
  frame = frame[0:512,:]

  print(counter)
  if cv2.waitKey(0) == 27:
    break
  
  label = np.zeros((512,512))
  polyPoint = np.array(polyPoint)
  cv2.fillPoly(label, pts = [polyPoint], color =(255,255,255))
  cv2.imshow("filledPolygon", label)
  
  cv2.imwrite(pathOutput+"image/"+str(counter)+".png",frame)
  cv2.imwrite(pathOutput+"label/"+str(counter)+".png",label)
  polyPoint = []
  checkedList[counter] == "y"


  # Break the loop
  # break



# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()