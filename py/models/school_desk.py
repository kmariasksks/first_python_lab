from .abstract_desk import AbstractDesk


class SchoolDesk(AbstractDesk):
    def __init__(self, height, width, length, has_tray, number_of_seats):
        super().__init__(height, width, length)
        self.has_tray = has_tray
        self.number_of_seats = number_of_seats

    def __str__(self):
        return f"{super().__str__()}, has_tray={self.has_tray}, number_of_seats={self.number_of_seats}"
