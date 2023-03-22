# import necessary packages

import cv2
import numpy as np
import mediapipe as mp
import SettingsModule
import HandLandmarkRecognition
import tensorflow as tf
import SettingsComponents.SettingsContainer as sc
import SettingsComponents.ToggleComponent as tc
import SettingsComponents.SliderBar as sb

# Define a new settings container to hold the components
settings_container = sc.SettingsContainer()

# Define some components to add to the settings menu
volume = sb.SliderBar("Volume", 50)
brightness = sb.SliderBar("Brightness", 20)
show_hands = tc.ToggleComponent("Show Hands", "Show", "Hide", True)
rgb = sb.SliderBar("RGB", 10)
# Add the components to the settings container
settings_container.add_component(volume)
settings_container.add_component(brightness)
settings_container.add_component(show_hands)
settings_container.add_component(rgb)

# Define new settings module, and assign settings container as one of the attributes
new_settings = SettingsModule.SettingsModule()
new_settings.settings_container = settings_container
# Run the webcam recognition for the module
new_settings.webcam_recognition()
