# Mediapipes hand landmarker is currently not supported on windows...

import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class HandLandmarkRecognition:
    base_options = None
    hand_landmarker = None
    hand_landmarker_options = None
    hand_landmarker_result = None
    vision_running_mode = None
    model_path = 'C:/Users/SLL125/PycharmProjects/GestureRecognition/mp_hand_landmark/' \
                 'hand_landmarker.task'

    # Responsible for initialising mediapipe, chosen model
    def __init__(self):
        self.__initialise_task()
        print("Hand landmark recognition class initialised")

    def __initialise_task(self):
        self.base_options = mp.tasks.BaseOptions
        self.hand_landmarker = mp.tasks.vision.HandLandmarker
        self.hand_landmarker_options = mp.tasks.vision.HandLandmarkerOptions
        self.vision_running_mode = mp.tasks.vision.RunningMode

        self.hand_landmarker_result = mp.tasks.vision.HandLandmarkerResult

        # Create a hand landmarker instance with the image mode:
        base_options = python.BaseOptions(model_asset_path=self.model_path)
        options = vision.HandLandmarkerOptions(base_options=base_options,
                                               num_hands=1)

        with self.hand_landmarker.create_from_options(options) as landmarker:
            print("Hand landmarker initialised")

    def webcam_recognition(self):
        # Initialize the webcam
        cap = cv2.VideoCapture(0)

        while True:
            # Read each frame from the webcam
            _, frame = cap.read()
            x, y, c = frame.shape

            # Flip the frame vertically
            frame = cv2.flip(frame, 1)

            framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Get hand landmark prediction
            result = self.hand_landmarker.process(framergb)

            # post process the result

            # Show the final output
            cv2.imshow("Output", frame)
            if cv2.waitKey(1) == ord('q'):
                break

        # release the webcam and destroy all active windows
        cap.release()
        cv2.destroyAllWindows()
