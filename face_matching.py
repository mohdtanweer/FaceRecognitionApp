import os, sys
import cv2
import time
import scipy
import numpy as np

from scipy import spatial

from app import app
from face_extraction import FaceExtraction
from face_embedding import FaceEmbedding

class FaceMatching():
    def __init__(self, selfie_img, id_img):
        self.selfie_img = app.config['S_UPLOAD_FOLDER'] + "/" + selfie_img
        self.id_img = app.config['I_UPLOAD_FOLDER'] + "/" + id_img
        self.detector_model_path = "face_detection_model/"
        self.embedding_model = "face_embedding_model/openface_nn4.small2.v1.t7"

    def match_selfie_id(self):
        id_img = cv2.imread(self.id_img)
        selfie_img = cv2.imread(self.selfie_img)

        # Get feature vector for ID image
        detect = FaceExtraction(id_img, self.detector_model_path)
        faces = detect.detect_face()
        print("0. Face detection done!")
        if len(faces) > 1:
            print("More than 1 faces detected in the ID image\nPlease provide another ID!!!")
        else:
            print(faces[0].shape)
            face_embedding_vec = FaceEmbedding(faces[0], self.embedding_model)
            embedding_vec_id = face_embedding_vec.get_face_embedding()

        # Get feature vector for Selfie image
        detect = FaceExtraction(selfie_img, self.detector_model_path)
        faces = detect.detect_face()
        if len(faces) > 1:
            print("More than 1 faces detected in the Selfie\nPlease provide another Selfie!!!")
        else:
            face_embedding_vec = FaceEmbedding(faces[0], self.embedding_model)
            embedding_vector_selfie = face_embedding_vec.get_face_embedding()
        
        similarity_dist = spatial.distance.cosine(embedding_vec_id, embedding_vector_selfie)
        print("Similarity between the images: {}".format(1 - similarity_dist))
        return 1 - similarity_dist