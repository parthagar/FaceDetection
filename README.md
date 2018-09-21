# Face Detection

### Requirements
You can install Conda for python which resolves all the dependencies for this project
or run 
`pip install requirements.txt`

### Description
I have combined Face Detection using Haar Features (which includes eye detection as well) and Face Detection using DNN model by taking inspiration and ideas from the references mentioned below.

#### Haar feature-based cascade classifiers
Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and Michael Jones in their paper, "Rapid Object Detection using a Boosted Cascade of Simple Features" in 2001. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.

#### DNN Model
The model is a ResNet10 architecture which takes in a 300x300 image and produces corresponding faces detected with their confidences. It is stored in two files - 1. The .caffemodel stores the weights and other parameters after training 2. The .prototxt file stores the network architecture.

### Execution
After reproducing the repo in your device, to run the code, type `python face_detection_combined.py`

### Functionalities
1) Sources of detection can be - Image file, Webcam feed, Video file
2) Detect faces by Haar features with/without eye detection (faster but less accurate and able to detect faces on when face is properly visible/aligned to image capturing point)
3) Detect faces by DNN model without eye detection (slower but more accurate and can detect faces at a variety of angles)

### To-do
1) Add FPS for the feed
2) Use threading for faster processing

### References
1) https://www.pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/
2) https://docs.opencv.org/master/d7/d8b/tutorial_py_face_detection.html

Thanks [Akshay Bahadur](https://github.com/akshaybahadur21/) for inspiring me!
