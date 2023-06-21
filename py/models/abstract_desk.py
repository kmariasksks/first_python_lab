"""
This module provides a AbstractDesk class for managing desks.
"""
from abc import ABC
from py.decorators.logging import logged  # pylint: disable=import-error
from py.exceptions.invalid_height_exception import InvalidHeightException  # pylint: disable=import-error


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

    def get_attributes_by_type(self, attr_type):
        """
        Returns a dictionary of attributes with values of the specified type.
        """
        attributes = self.__dict__
        return {key: value for key, value in attributes.items() if isinstance(value, attr_type)}

    @logged(InvalidHeightException, "file")
    def check_height(self):
        """
        Exception raised when an invalid height is encountered.
        """

        if self.height > 200:
            raise InvalidHeightException
