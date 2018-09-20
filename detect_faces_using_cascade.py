import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_detector = cv2.CascadeClassifier('haarcascade_eye.xml')

# Video with eye detection
def __Video_with_eye_detection(src):
    stream = cv2.VideoCapture(src)

    while True:
        _, color_frame = stream.read()

        gray_frame = cv2.cvtColor(color_frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray_frame)

        for (fx, fy, fw, fh) in faces:
            cv2.rectangle(color_frame, (fx, fy), (fx + fw, fy + fh), (0, 0, 255), 3)

            roi_color = color_frame[fy : fy + fh, fx : fx + fw]
            roi_gray = gray_frame[fy : fy + fh, fx : fx + fw]

            eyes = eye_detector.detectMultiScale(roi_gray, scaleFactor = 1.1, minNeighbors = 10, minSize = (20, 20),
                                                 flags = cv2.CASCADE_SCALE_IMAGE)

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)


        cv2.imshow('Feed', color_frame)

        k = cv2.waitKey(30) & 0xFF
        # 32 is the code for spacebar button
        if k == 32:
            break

    stream.release()

# Video without eye detection
def __Video_without_eye_detection(src):
    stream = cv2.VideoCapture(src)

    while True:
        _, color_frame = stream.read()

        gray_frame = cv2.cvtColor(color_frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray_frame)

        for (fx, fy, fw, fh) in faces:
            cv2.rectangle(color_frame, (fx, fy), (fx + fw, fy + fh), (0, 0, 255), 3)

        cv2.imshow('Feed', color_frame)

        k = cv2.waitKey(30) & 0xFF
        # 32 is the code for spacebar button
        if k == 32:
            break

    stream.release()

# Image with eye detection
def __Image_with_eye_detection(img):
    color_frame = cv2.imread(img)

    gray_frame = cv2.cvtColor(color_frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_frame)

    for (fx, fy, fw, fh) in faces:
        cv2.rectangle(color_frame, (fx, fy), (fx + fw, fy + fh), (0, 0, 255), 3)

        roi_color = color_frame[fy : fy + fh, fx : fx + fw]
        roi_gray = gray_frame[fy : fy + fh, fx : fx + fw]

        eyes = eye_detector.detectMultiScale(roi_gray, scaleFactor = 1.1, minNeighbors = 10, minSize = (20, 20),
                                             flags = cv2.CASCADE_SCALE_IMAGE)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)


    cv2.imshow('Feed', color_frame)

    while True:
        k = cv2.waitKey(30) & 0xFF
        if k == 32:
            break

# Image without eye detection
def __Image_without_eye_detection(img):
    color_frame = cv2.imread(img)

    gray_frame = cv2.cvtColor(color_frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_frame)

    for (fx, fy, fw, fh) in faces:
        cv2.rectangle(color_frame, (fx, fy), (fx + fw, fy + fh), (0, 0, 255), 3)

    cv2.imshow('Feed', color_frame)

    while True:
        k = cv2.waitKey(30) & 0xFF
        if k == 32:
            break


def detect_faces_using_cascade(choice = 1):
    if choice == 1:
        choice = input('Enter video source: ')
        __Video_with_eye_detection(int(choice) if choice.isdigit() else str(choice))
    elif choice == 2:
        choice = input('Enter video source: ')
        __Video_without_eye_detection(int(choice) if choice.isdigit() else str(choice))
    elif choice == 3:
        __Image_with_eye_detection(str(input('Enter image name/path: ')))
    elif choice == 4:
        __Image_without_eye_detection(str(input('Enter image name/path: ')))
    else:
        print("Wrong choice!")
