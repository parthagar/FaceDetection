from detect_faces_using_cascade import detect_faces_using_cascade
from detect_faces_using_model import detect_faces_using_model

print('Using what?\n'
      '1. Haar Cascades (Faster but less accurate and only detects face is parallel to capturing point\n'
      '2. DNN Model (Slower but more accurate and can detect face at a variety of angles')

choice = int(input())

print('1. Cam feed without eye detection\n'
      '2. Image without eye detection')
if choice == 1:
    print('3. Cam feed with eye detection\n'
          '4. Image with eye detection')
    detect_faces_using_cascade(int(input()))
elif choice == 2:
    detect_faces_using_model(int(input()))
else:
    print('Wrong choice')