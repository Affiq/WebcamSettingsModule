import cv2
from SettingsComponents.RectangleButton import RectangleButton
from SettingsComponents.Submenu import Submenu


class SettingsContainer():
    def __init__(self):
        # Parameters used for calculation
        self.submenu = Submenu()
        self.submenu_button_size = None
        self.close_button = None
        self.close_button_size = 25
        self.Components = []
        self.Chunked_components = []
        self.button_width = 0
        self.button_bounds = []
        self.y1, self.y2 = 0, 0
        self.state = "menu"
        self.current_component = None
        self.current_submenu = 0
        # Customizable parameters
        self.num_buttons = 3
        self.y_offset = 20
        self.x_offset = 20
        self.button_height = 60

    def show_settings(self, frame, pointer_coords, gesture):
        if self.state == "menu":
            self.draw_menu(frame)
            self.__detect_button_point(pointer_coords)
            self.__detect_close_button_point(pointer_coords)
            self.submenu.detect_button_point(pointer_coords)
            self.current_submenu = int(self.submenu.current_submenu)
        elif self.state == "component":
            self.current_component.draw(frame)
            self.current_component.detect_pointer(pointer_coords)
            if gesture == "thumbs up":  # If thumbs up given, return to main menu
                self.state = "menu"

    def draw_menu(self, frame):
        self.draw_buttons(frame, self.current_submenu)
        self.draw_close_button(frame)
        self.submenu.draw(frame, self.Chunked_components)

    # Function used to draw each button for each SettingComponent...
    def draw_buttons(self, frame, submenu_num):
        y, x, c = frame.shape
        # First we calculate the width relative to frame size
        self.calculate_button_width(x)
        # Initialise offset for the button UI
        x2 = self.x_offset
        self.y2 = y - self.y_offset
        self.y1 = int(y - self.y_offset - self.button_height)
        # Iteratively calculate the variable x1 and x2 positions for the buttons...
        for component in self.Chunked_components[submenu_num]:
            x1 = int(x2)
            x2 = int(x1 + self.button_width)
            # Draw the border - need to refactor
            cv2.rectangle(frame, (x1, self.y2), (x2, self.y1),
                          (255, 255, 255), 2)
            # Define the button and draw it
            menu_button = RectangleButton(component.name, (x1, self.y2), (x2, self.y1),
                                          (50, 50, 50))
            menu_button.draw(frame)
            menu_button.draw_label(frame, component.name)
            # We add the button bounds here...
            self.button_bounds.append([menu_button, component])

    # Get width of each button
    def calculate_button_width(self, x):
        self.button_width = (x - (2 * self.x_offset)) / self.num_buttons

    # Recalculate the chunked component list after adding a new component
    def add_component(self, component):
        self.Components.append(component)
        self.Chunked_components = self.__split_component_list(self.Components,
                                                              self.num_buttons)
        # Convert iterator to a list
        self.Chunked_components = list(self.Chunked_components)

    # Detect pointer for choosing buttons...
    def __detect_button_point(self, pointer_coords):
        for button_boundary in self.button_bounds:
            current_button = button_boundary[0]
            current_component = button_boundary[1]
            if current_button.detect_button_point(pointer_coords):
                self.__toggle_to_component_state(current_component)

    def draw_close_button(self, frame):
        y, x, c = frame.shape
        self.close_button = RectangleButton("CloseButton",
                                            (x - self.close_button_size, 0),
                                            (x, self.close_button_size),
                                            (50, 50, 200))
        self.close_button.draw(frame)

    def __detect_close_button_point(self, pointer_coords):
        if self.close_button.detect_button_point(pointer_coords):
            self.toggle_hidden()

    def toggle_hidden(self):
        if self.state == "menu":
            self.state = "hidden"

    def __toggle_to_component_state(self, component):
        self.current_component = component
        self.state = "component"

    @staticmethod
    def __split_component_list(component_list, chunk_size):
        for i in range(0, len(component_list), chunk_size):
            yield component_list[i:i + chunk_size]

