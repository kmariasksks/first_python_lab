"""
This model provides a SchoolDesk class.
"""
from .abstract_desk import AbstractDesk


class SchoolDesk(AbstractDesk):  # pylint: disable=too-few-public-methods
    """
        A class representing a journal desk.
        Inherits from the AbstractDesk class.
    """

    # pylint: disable=too-many-arguments
    def __init__(self, height, width, length, has_tray, number_of_seats):
        super().__init__(height, width, length)
        self.has_tray = has_tray
        self.number_of_seats = number_of_seats

    def __str__(self):
        return f"{super().__str__()}, has_tray={self.has_tray}, " \
               f"number_of_seats={self.number_of_seats}"
