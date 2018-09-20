import cv2
import imutils
import numpy as np

model = cv2.dnn.readNetFromCaffe('deploy.prototxt.txt', 'res10_300x300_ssd_iter_140000.caffemodel')

# Video without eye detection
def __Video_without_eye_detection(src):
    stream = cv2.VideoCapture(src)

    while True:
        _, color_frame = stream.read()
        color_frame = imutils.resize(color_frame, width = 400)

        (h, w) = color_frame.shape[: 2]
        blob = cv2.dnn.blobFromImage(cv2.resize(color_frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

        model.setInput(blob)
        faces = model.forward()

        for i in range(0, faces.shape[2]):

            confidence =  faces[0, 0, i, 2]

            if confidence < 0.5:
                continue

            box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(color_frame, (startX, startY), (endX, endY),
                          (0, 0, 255), 2)
            cv2.putText(color_frame, text, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

        cv2.imshow('Feed', color_frame)

        k = cv2.waitKey(1) & 0xFF
        # 32 is the code for spacebar button
        if k == 32:
            break

    stream.release()

# Image without eye detection
def __Image_without_eye_detection(img):
    color_frame = cv2.imread(img)

    (h, w) = color_frame.shape[: 2]
    blob = cv2.dnn.blobFromImage(cv2.resize(color_frame, (300, 300), 1.0, (300, 300), (104.0, 177.0, 123.0)))

    model.setInput(blob)
    faces = model.forward()

    for i in range(0, faces.shape[2]):

        confidence = faces[0, 0, i, 2]

        if confidence < 0.5:
            continue

        box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(color_frame, (startX, startY), (endX, endY),
                      (0, 0, 255), 2)
        cv2.putText(color_frame, text, (startX, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

    cv2.imshow('Image', color_frame)


def detect_faces_using_model(choice = 1):
    if choice == 1:
        choice = input('Enter video source: ')
        __Video_without_eye_detection(int(choice) if choice.isdigit() else str(choice))
    elif choice == 2:
        __Image_without_eye_detection(str(input("Enter image name/path: ")))
    else:
        print("Wrong choice!")
