"""
This module provides a AbstractDesk class for managing desks.
"""
from abc import ABC


class AbstractDesk(ABC):  # pylint: disable=too-few-public-methods
    """
        AbstractDesk is an abstract base class representing a generic desk.
    """
    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length

    def __str__(self):
        return f"height={self.height}, width={self.width}, length={self.length}"

    def add_max_width(self):
        """
        :return: maximum available width
        """
        pass

    def get_attributes_by_type(self, attr_type):
        """
        Returns a dictionary of attributes with values of the specified type.
        """
        attributes = self.__dict__
        return {key: value for key, value in attributes.items() if isinstance(value, attr_type)}
