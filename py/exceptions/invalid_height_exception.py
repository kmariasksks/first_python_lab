"""
This module defines custom exception classes related to height.
"""


class InvalidHeightException(Exception):
    """
    Exception raised when an invalid height is encountered.
        Attributes:
            message (str): The error message describing the invalid height.
    """
    message = "Height should be less than 200!"

    def __init__(self):
        super().__init__(self.message)
