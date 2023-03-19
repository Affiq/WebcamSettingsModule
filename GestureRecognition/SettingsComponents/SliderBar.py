import cv2
import SettingsComponents.SettingsComponent as sc


class SliderBar(sc.SettingsComponent):
    # Parameters for name and value of slider bar
    name = None
    value = None
    frame = None

    # Variables used by functions to update coordinates
    x, y = 0, 0
    x1, x2, y1, y2 = 0, 0, 0, 0

    # Parameters for slider bar UI
    y_offset = 40
    x_offset = 20
    slider_height = 40
    # Button parameters
    slider_button_width = 30
    slider_width = 0

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value

    def calculate_slider_bounds(self):
        # Calculate coordinates for drawing entire bar
        self.slider_width = self.x - (2 * self.x_offset)
        self.x1 = self.x_offset
        self.x2 = self.x_offset + self.slider_width
        self.y1 = self.y_offset
        self.y2 = self.y_offset + self.slider_height

    # The slider bar will appear near the top.
    # We must calculate the coordinates before drawing...
    def draw(self, frame):
        # Calculate coordinates for drawing slider bar background
        self.frame = frame
        self.y, self.x, c = frame.shape
        self.calculate_slider_bounds()
        # Draw outer rectangle
        cv2.rectangle(self.frame, (self.x1, self.y2), (self.x2, self.y1), (50, 50, 50), -1)

        # Calculate coordinates for slider button
        button_center_x = int(self.slider_width * (self.value / 100) + self.x_offset)
        button_center_y = int(self.y_offset + (int(self.slider_height / 2)))
        b_top_left = [button_center_x - int(self.slider_button_width / 2),
                      button_center_y - int(self.slider_height / 2)]
        b_bottom_right = [button_center_x + int(self.slider_button_width / 2),
                          button_center_y + int(self.slider_height / 2)]
        # Draw the slider button
        cv2.rectangle(self.frame, b_top_left, b_bottom_right, (0, 150, 0), -5)

        # Draw the value display
        cv2.rectangle(self.frame, (5, self.y-5), (205, self.y-65), (50,50,50), -1)
        cv2.putText(frame, self.name + ": " + str(self.value), (20, self.y-20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 1, cv2.LINE_AA)


    # Detect if pointer is within the slider bounds
    def detect_pointer(self, pointer_coords):
        px, py = pointer_coords[0], pointer_coords[1]
        if (px > self.x1) and (px < self.x2):
            if (py > self.y1) and (py < self.y2):
                # Calculate the supposed new value...
                x_diff = px - self.x_offset  # Get the x position relative to slider
                x_diff_normalised = x_diff / self.slider_width
                # Assign the new value
                self.value = int(x_diff_normalised * 100)

