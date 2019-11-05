import cv2
vidcap = cv2.VideoCapture('10000000_3-22-2019_11.28.54.avi')
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  title_number = count
  cv2.imwrite("frame%d.jpg" % title_number, image)     # save frame as JPEG file
  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  count += 1
