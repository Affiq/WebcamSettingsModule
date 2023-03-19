# import necessary packages

import cv2
import numpy as np
import mediapipe as mp
import HandGestureRecognition
import HandLandmarkRecognition
import tensorflow as tf
from tensorflow.keras.models import load_model

HGR = HandGestureRecognition.HandGestureRecognition();
HGR.webcam_recognition()
