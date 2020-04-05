# Face Matching Flask App

## Introduction 
This project is do find similarity between two images. It uses the deep learning features of OpenCV and is developed by following the guide of PyImageSearch.
It uses the pre-trained Caffe deep learning model provided by OpenCV to detect faces.
The face recognition model OpenCV uses to compute the 128-d face embeddings comes from the [OpenFace project](https://cmusatyalab.github.io/openface/)

## Getting Started

## Software Dependencies
Refer to requirements.txt

## User Guide

### Build Docker Image
1. Come to FaceRecognitionApp directory
2.  Build the docker image : `docker build -t face_matching .`

### Run Docker Image
Now the Docker Image is created, we need to run the image in the container:
`docker run -p 8888:5000 --name face_matching face_matching`

### Input
Sample input:
```
curl -X POST -F 'selfie=@/Users/user/Documents/Personal/revoex/selfie_images/IMG001.jpg' -F 'id=@/Users/user/Documents/Personal/revoex/id_images/IMG-1978.jpg' http://0.0.0.0:8888/match'
```

Sample output:
```
{
  "id_filename": "IMG-1978.jpg", 
  "reason": "Selfie and ID Image uploaded successfully!", 
  "score": 0.9471489787101746, 
  "selfie_filename": "IMG001.jpg", 
  "status": 0
}```


