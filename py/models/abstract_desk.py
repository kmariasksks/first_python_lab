from abc import ABC


class AbstractDesk(ABC):
    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length

    def __str__(self):
        return f"height={self.height}, width={self.width}, length={self.length}"
