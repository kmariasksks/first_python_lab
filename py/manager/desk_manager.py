"""
Desk Manager class
"""


from py.models.coffee_table import CoffeeTable
from py.models.journal_desk import JournalDesk
from py.models.school_desk import SchoolDesk
from py.models.writing_desk import WritingDesk


class DeskManager:
    """
    Desk Manager class
    This class manages a collection of desks and provides methods to search desks.
    """
    def __init__(self):
        self.desks = []

    def add_desk(self, desk_s):
        """
        Adds a desk to the list of desks.
        """
        self.desks.append(desk_s)

    def find_desk_with_height(self, height):
        """
        Finds desks with a specific height.
        """
        return [desk_s for desk_s in self.desks if desk_s.get_height() == height]

    def find_desk_with_width_more_than(self, width):
        """
        Finds desks with a width greater than a given value.
        """
        return [desk_s for desk_s in self.desks if desk_s.get_width() > width]

    def find_desk_with_length_less_than(self, length):
        """
        Finds desks with a length less than a given value.
        """
        return [desk_s for desk_s in self.desks if desk_s.get_length() < length]

    def __len__(self):
        """
        Returns the length of the list of desks.
        """
        return len(self.desks)

    def __getitem__(self, index):
        """
        Returns the desk at the given index.
        """
        return self.desks[index]

    def __iter__(self):
        """
        Returns an iterator over the list of desks.
        """
        return iter(self.desks)

    def execute_method_for_desks(self, method_name):
        """
        Executes a method from the AbstractDesk class for all desks in the manager
        and returns a list of concatenated strings of the object and its index.
        """
        results = []
        for index, desk_s in enumerate(self.desks):
            if hasattr(desk_s, method_name):
                method = getattr(desk_s, method_name)
                result = method()
                result_str = f"Object at index {index}: {desk_s} - Result: {result}"
                results.append(result_str)
        return results

    def execute_method_with_results(self, method_name):
        """
        Executes a method from the AbstractDesk class for all desks in the manager
        and returns a list of concatenated strings of the object and its corresponding method result
        """
        results = []
        for desk_s, result in zip(self.desks, self.execute_method_for_desks(method_name)):
            result_str = f"Object: {desk_s} - Result: {result}"
            results.append(result_str)
        return results

    def check_condition(self):
        """
        Checks if all objects in the manager satisfy the given conditions
        and if any object satisfies the conditions.
        Returns a dictionary with keys "all" and "any" and corresponding boolean values.
        """

        def condition_height(desk_s):
            return desk_s.height == 60

        def condition_width(desk_s):
            return desk_s.width < 35

        def condition_length(desk_s):
            return desk_s.length > 80

        all_result = all(condition_height(desk_s) and condition_width(desk_s)
                         and condition_length(desk_s) for desk_s in self.desks)
        any_result = any(condition_height(desk_s) and condition_width(desk_s)
                         and condition_length(desk_s) for desk_s in self.desks)

        return {"all": all_result, "any": any_result}


desk_manager = DeskManager()
desk_manager.add_desk(WritingDesk(100, 40, 50, 100, 105))
desk_manager.add_desk(WritingDesk(80, 35, 60, 80, 95))
desk_manager.add_desk(CoffeeTable(75, 38, 70, 0, 6))
desk_manager.add_desk(CoffeeTable(70, 33, 80, 4, 4))
desk_manager.add_desk(JournalDesk(60, 37, 65, True, 105))
desk_manager.add_desk(JournalDesk(65, 42, 68, False, 115))
desk_manager.add_desk(SchoolDesk(58, 20, 90, True, 2))
desk_manager.add_desk(SchoolDesk(74, 30, 100, False, 2))

for desk in desk_manager:
    print(desk)
    print("\n")
