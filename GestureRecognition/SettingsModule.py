# import necessary packages

import cv2
import numpy as np
import mediapipe as mp
import SettingsComponents.SliderBar as sb
import SettingsComponents.SettingsContainer as sc
import SettingsComponents.ToggleComponent as tc
import tensorflow as tf
from tensorflow.keras.models import load_model

class SettingsModule:
    mpHands = None
    hands = None
    mpDraw = None
    model = None
    classNames = None

    # Responsible for initialising mediapipe, chosen model and classnames
    def __init__(self):
        self.__initialise_mp()
        self.__initialise_model()
        self.__initialise_class_names()
        self.settings_container = None
        print("Hand recognition class initialised")

    def __initialise_mp(self):
        # initialize Mediapipe
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        self.mpDraw = mp.solutions.drawing_utils

    def __initialise_model(self):
        # Load the gesture recognizer model
        self.model = load_model('mp_hand_gesture')

    def __initialise_class_names(self):
        # Load class names
        f = open('gesture.names', 'r')
        self.classNames = f.read().split('\n')
        f.close()
        print(self.classNames)

    def webcam_recognition(self):
        # Initialize the webcam for Hand Gesture Recognition Python project
        cap = cv2.VideoCapture(0)

        # Main loop calculates landmarks and hand gestures...
        index_tip = [0, 0]
        gesture = None
        while True:
            # Read each frame from the webcam and get dimensions
            _, frame = cap.read()
            y, x, c = frame.shape
            # Flip the frame vertically
            frame = cv2.flip(frame, 1)

            framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # volume.draw_slider_bar(frame)
            # settings_container.draw_buttons(frame)

            # Get hand landmark prediction
            result = self.hands.process(framergb)
            self.settings_container.show_settings(frame, index_tip, gesture)

            # post process the result
            if result.multi_hand_landmarks:
                for handslms in result.multi_hand_landmarks:
                    landmarks = self.calculate_landmarker_coordinates(result, x, y)
                    # print("Palm coordinates: " + ':'.join(str(x) for x in landmarks[0]))

                    # Drawing landmarks on frames
                    self.draw_all_handlandmarks(frame, handslms)
                    self.draw_index_finger_tip(frame, landmarks)
                    index_tip = landmarks[8]
                    # volume.set_value(volume.detect_pointer(index_tip))
                    # settings_container.show_settings(frame, index_tip)

                    # Predict gesture in Hand Gesture Recognition project
                    prediction = self.model.predict([landmarks])

                    # print(prediction)
                    classID = np.argmax(prediction)
                    className = self.classNames[classID]
                    gesture = className

                    # show the gesture prediction on the frame
                    # cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    #            1, (0, 0, 255), 2, cv2.LINE_AA)

            # Show the final output
            cv2.imshow("Output", frame)
            if cv2.waitKey(1) == ord('q'):
                break

        # release the webcam and destroy all active windows
        cap.release()
        cv2.destroyAllWindows()

    # x, y are the frames width and height respectively
    # Used to calculate a landmark for a hand
    def calculate_landmarker_coordinates(self, result, x, y):
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])
        return landmarks

    def draw_all_handlandmarks(self, frame, handslms):
        self.mpDraw.draw_landmarks(frame, handslms, self.mpHands.HAND_CONNECTIONS)

    def draw_index_finger_tip(self, frame, landmarks):
        index_tip = landmarks[8]
        cv2.circle(frame, index_tip, 5, (0, 255, 0), -1)


