from py.models.coffee_table import CoffeeTable
from py.models.journal_desk import JournalDesk
from py.models.school_desk import SchoolDesk
from py.models.writing_desk import WritingDesk


class DeskManager:
    def __init__(self):
        self.desks = []

    def add_writing_desk(self, desk):
        self.desks.append(desk)

    def find_desk_with_height(self, height):
        return [desk for desk in self.desks if desk.get_height() == height]

    def find_desk_with_width_more_than(self, width):
        return [desk for desk in self.desks if desk.get_width() > width]

    def find_desk_with_length_less_than(self, length):
        return [desk for desk in self.desks if desk.get_length() < length]


desk_manager = DeskManager()
desk_manager.add_writing_desk(WritingDesk(100, 40, 50, 100, 105))
desk_manager.add_writing_desk(WritingDesk(80, 35, 60, 80, 95))
desk_manager.add_writing_desk(CoffeeTable(75, 38, 70, 0, 6))
desk_manager.add_writing_desk(CoffeeTable(70, 33, 80, 4, 4))
desk_manager.add_writing_desk(JournalDesk(60, 37, 65, True, 105))
desk_manager.add_writing_desk(JournalDesk(65, 42, 68, False, 115))
desk_manager.add_writing_desk(SchoolDesk(58, 20, 90, True, 2))
desk_manager.add_writing_desk(SchoolDesk(74, 30, 100, False, 2))

for desk in desk_manager.desks:
    print(desk)

    print("\n")
