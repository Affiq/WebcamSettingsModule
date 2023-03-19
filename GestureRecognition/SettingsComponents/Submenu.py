import cv2
from SettingsComponents.RectangleButton import RectangleButton
from SettingsComponents.SettingsComponent import SettingsComponent


class Submenu(SettingsComponent):
    def __init__(self):
        super().__init__()
        self.submenu_button_size = None
        self.current_submenu = 0
        self.submenu_button_list = []

    def draw(self, frame, chunked_components):
        self.submenu_button_size = 60
        y2 = 0
        for x, submenu in enumerate(chunked_components):
            y1 = y2
            y2 = y1 + self.submenu_button_size
            submenu_button = RectangleButton(str(x),
                                             (0, y1),
                                             (self.submenu_button_size, y2),
                                             (50, 50, 50))
            submenu_button.draw(frame)
            submenu_button.draw_border(frame, (255, 255, 255))
            submenu_button.draw_label(frame, str(x))
            self.submenu_button_list.append(submenu_button)

    def detect_button_point(self, pointer_coords):
        for button in self.submenu_button_list:
            if button.detect_button_point(pointer_coords):
                self.current_submenu = button.name
        return self.current_submenu


