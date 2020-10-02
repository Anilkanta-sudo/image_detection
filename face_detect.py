import cv2
from random import randrange

# trained model of faces
trained_face_data = cv2.CascadeClassifier("/home/smsc/Documents/Detection/face_default.xml")

# image to detect face
img = cv2.imread('dance.jpg')
# to capture a video,0 default cam, add path
#webcam = cv2.VideoCapture(0)

gray_scale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
coordinates_face = trained_face_data.detectMultiScale(gray_scale_img)

# adding up coordinates and drawing rectangle shape on to the face to identify
for (x, y, w, h) in coordinates_face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (randrange(255), randrange(255), randrange(255)), 2)
cv2.imshow("face detect", img)
# waitkey for displaying
cv2.waitKey()
# loop forever for over frames
"""while True:
    # read the current frames
    # frame_read-True/false-always True, frame-image-from cam
    frame_read, frame = webcam.read()

    # change color to black and white
    gray_scale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # finding cordinates
    coordinates_face = trained_face_data.detectMultiScale(gray_scale_img)

    # adding up coordinates and drawing rectangle shape on to the face to identify
    for (x, y, w, h) in coordinates_face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(255), randrange(255), randrange(255)), 2)

    # show image
    cv2.imshow("face detect", frame)

    # waitkey for displaying
    cv2.waitKey(1)
"""