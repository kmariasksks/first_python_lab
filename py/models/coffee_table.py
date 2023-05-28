from .abstract_desk import AbstractDesk


class CoffeeTable(AbstractDesk):
    def __init__(self, height, width, length, number_of_drawers, number_of_guests):
        super().__init__(height, width, length)
        self.number_of_drawers = number_of_drawers
        self.number_of_guests = number_of_guests

    def __str__(self):
        return super().__str__() + f", numberOfDrawers={self.number_of_drawers}, numberOfGuests={self.number_of_guests}"
