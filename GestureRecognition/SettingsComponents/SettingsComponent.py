from abc import abstractmethod


class SettingsComponent:
    def __init__(self):
        self.name = ""
        self.value = ""

    @abstractmethod
    def draw(self):
        pass
