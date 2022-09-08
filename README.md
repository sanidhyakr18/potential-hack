# Mirror Ball

## Motivation

Lack of resources like infrastructure and coaching in Sports Industry is a major problem and especially during the pandemic these resources are not accessible sitting at home.
Also, the industry is not welcoming to the newcomers except prodigies! So how can you succeed at improving your stance or hit the perfect cover drive like Virat Kohli and upskill yourself to show that you can be the best?

We have the solution!!


## Introduction

The app is developed using the [ML Kit Quickstart app](https://github.com/googlesamples/mlkit.git).

The WebApp is developed using OpenCV, TensorFlow, OpenPose and Mediapipe.

We have documented the points of a person who is performing a certain activity as our model. Using the points we can check how similar a test video is to that particular activity. 

e.g. How close are you to performing Virat Kohli's cover drive to perfection


## Releases
The apk file can be found [Here](https://github.com/sanidhyakr18/potential-hack/blob/main/apk/Mirror%20Ball.apk).


## Getting Started

* [MirrorBall](https://github.com/sanidhyakr18/potential-hack/tree/main/MirrorBall) folder contains the app source code
* [APK](https://github.com/sanidhyakr18/potential-hack/tree/main/apk) folder contains the APK file
* [Human-Pose-Compare-master](https://github.com/sanidhyakr18/potential-hack/tree/main/E-hack/Human-Pose-Compare-master) folder contains the WebApp to illustrate how the correctness score is calculated.


## How to use the Web App

1. Downlaod the zip folder into a directory
2. Use pip install -r requirements.txt to download the dependencies.
3. Inside the directory run "streamlit run main.py" to run the pyhton code and you're good to go.

## How to use the Mobile App
1. It uses the mobile camera preview as input and contains the pose detection API workflow
2. The user selects an activity that he wants to practice
3. The app compares it with the predifined activity and outputs result in the form of a stick figure
4. When the output coordinates are close to the predefined pose the lines get greener in color and when they are not the lines get red. 
5. This is to give visual feedback on the pose comparison. 


## Feature List
* Detect the position of the human body in real time.
* Give feedback to user if practicing in correctly just like a personal coach/trainer
* Coordinate Smoothing
* Pose Comparison
* Dynamic drawing function

## Support

* [Documentation](https://developers.google.com/ml-kit/guides)
* [API Reference](https://developers.google.com/ml-kit/reference/android)
* [Stack Overflow](https://stackoverflow.com/questions/tagged/google-mlkit)
* [OpenCV](https://opencv.org/)
* [Mediapipe](https://mediapipe.dev/)
