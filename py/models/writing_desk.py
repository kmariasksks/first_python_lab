"""
This model provides a WritingDesk class.
"""
from .abstract_desk import AbstractDesk


class WritingDesk(AbstractDesk):  # pylint: disable=too-few-public-methods
    """
        A class representing a journal desk.
        Inherits from the AbstractDesk class.
    """

    # pylint: disable=too-many-arguments
    def __init__(self, height, width, length, current_height, max_height):
        super().__init__(height, width, length)
        self.current_height = current_height
        self.max_height = max_height

    def adjust_height(self, centimeters):
        """
           Adjusts the current height of the desk by the specified number of centimeters.
        """
        new_height = self.current_height + centimeters
        if new_height <= self.max_height:
            self.current_height = new_height

    def move_down(self, centimeters):
        """
           Moves the desk down by the specified number of centimeters.
        """
        new_height = self.current_height - centimeters
        if new_height >= 0:
            self.current_height = new_height

    def __str__(self):
        return f"{super().__str__()}, current_height={self.current_height}," \
               f" max_height={self.max_height}"
