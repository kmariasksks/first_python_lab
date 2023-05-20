from .abstract_desk import AbstractDesk


class WritingDesk(AbstractDesk):
    def __init__(self, height, width, length, current_height, max_height):
        super().__init__(height, width, length)
        self.current_height = current_height
        self.max_height = max_height

    def adjust_height(self, centimeters):
        new_height = self.current_height + centimeters
        if new_height <= self.max_height:
            self.current_height = new_height

    def move_down(self, centimeters):
        new_height = self.current_height - centimeters
        if new_height >= 0:
            self.current_height = new_height

    def __str__(self):
        return f"{super().__str__()}, current_height={self.current_height}, max_height={self.max_height}"
