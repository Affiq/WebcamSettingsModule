import cv2
import SettingsComponents.SettingsComponent as sc


class RectangleButton(sc.SettingsComponent):
    def __init__(self, name, top_left, bottom_right, bgr):
        self.name = name
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.bgr = bgr
        self.__calculate_coords()

    def __calculate_coords(self):
        self.x1 = self.top_left[0]
        self.x2 = self.bottom_right[0]
        self.y1 = self.top_left[1]
        self.y2 = self.bottom_right[1]
        # Needed to readjust the coordinates
        if self.x1 > self.x2:
            self.x1 = self.x2
            self.x2 = self.top_left[0]
        if self.y1 > self.y2:
            self.y1 = self.y2
            self.y2 = self.top_left[1]

    def draw_label(self, frame, text):
        cv2.putText(frame, text, (self.x1+2, self.y2-5), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255, 255, 255), 1, cv2.LINE_AA)

    def draw(self, frame):
        cv2.rectangle(frame, self.top_left,
                      self.bottom_right,
                      self.bgr, -1)

    def draw_border(self, frame, bgr):
        cv2.rectangle(frame, self.top_left,
                      self.bottom_right,
                      bgr, 2)

    def get_y_centre(self):
        return int((self.y2 + self.y1)/2)

    # Detect if the pointer is within the bounds
    def detect_button_point(self, pointer_co_ords):
        px, py = pointer_co_ords[0], pointer_co_ords[1]
        if (px > self.x1) and (px < self.x2):
            if (py > self.y1) and (py < self.y2):
                return True
        return False

    def on_detect_button_point(self, pointer_co_ords, func):
        if self.detect_button_point(pointer_co_ords):
            print("Executing button detection func")
            func()
        else:
            print("The function should not execute")
