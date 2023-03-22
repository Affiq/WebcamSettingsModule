import SettingsComponents.SettingsComponent as sc
import SettingsComponents.RectangleButton as rb
import cv2


class ToggleComponent(sc.SettingsComponent):
    def __init__(self, name, label1, label2, default_value):
        self.boundary2 = None
        self.boundary1 = None
        self.name = name
        self.label1 = label1
        self.label2 = label2
        self.value = default_value
        # Parameters for slider bar UI
        self.y_offset = 40
        self.width = 300
        self.height = 40
        self.label_width = 80

    # Create two rectangle button components
    def draw(self, frame):
        y, x, c = frame.shape
        
        # Calculate boundary1 coordinates
        x1 = int((x - self.width)/2)
        x2 = int(x1 + (self.width/2))
        top_left = (x1, int(self.y_offset))
        bottom_right = (x2, int(self.y_offset + self.height))
        # Draw boundary1
        self.boundary1 = rb.RectangleButton("Background", top_left, bottom_right, (50, 50, 50))
        self.boundary1.draw(frame)
        
        # Calculate boundary2 coordinates
        # Calculate boundary1 coordinates
        x1 = x2  # Use old x2 coordinates
        x2 = int(x1 + (self.width/2))
        top_left = (x1, int(self.y_offset))
        bottom_right = (x2, int(self.y_offset + self.height))
        # Draw boundary2
        self.boundary2 = rb.RectangleButton("Background", top_left, bottom_right, (50, 50, 50))
        self.boundary2.draw(frame)
        self.draw_indicator(frame)
        self.draw_labels(frame)

    def draw_indicator(self, frame):
        radius = int(self.height / 2)
        if self.value:
            xcoord = self.boundary1.x1 + radius
        else:
            xcoord = self.boundary2.x2 - radius
        coordinates = (xcoord, self.boundary2.get_y_centre())
        cv2.circle(frame, coordinates, radius, (255,255,255), -1)

    def draw_labels(self, frame):
        # Drawing label box
        first_coords = ((self.boundary1.x1 - self.label_width), self.boundary1.y1)
        second_coords = (self.boundary1.x1, self.boundary1.y2)
        labelbox1 = rb.RectangleButton("Label1", first_coords, second_coords, (100, 100, 100))
        labelbox1.draw(frame)
        labelbox1.draw_label(frame, self.label1)
        # Drawing second label box
        first_coords = (self.boundary2.x2, self.boundary2.y1)
        second_coords = ((self.boundary2.x2 + self.label_width), self.boundary2.y2)
        labelbox2 = rb.RectangleButton("Label2", first_coords, second_coords, (100, 100, 100))
        labelbox2.draw(frame)
        labelbox2.draw_label(frame, self.label2)

    def set_size(self, y_off, width, height):
        self.y_offset = y_off
        self.width = width
        self.height = height

    def set_true(self):
        self.value = True

    def set_false(self):
        self.value = False

    def detect_pointer(self, pointer_coords):
        if self.boundary1.detect_button_point(pointer_coords):
            self.value = True
        if self.boundary2.detect_button_point(pointer_coords):
            self.value = False
