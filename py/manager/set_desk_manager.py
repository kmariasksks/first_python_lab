"""
Set Manager class
"""


class SetManager:
    """
    This class manages sets of objects from a regular manager.
    It provides functionality for based on the favorite sets
    """

    def __init__(self, manager_regulation):
        """
        Initializes a new instance of the SetManager class.
        :param manager_regulation: The regular manager containing the objects.
        """
        self.manager_regulation = manager_regulation

    def __iter__(self):
        """
        Returns an iterator that iterates over the objects in the combined favorite sets.
        """
        for desk in self.manager_regulation:
            for item in desk.favorite_set:
                yield item

    def __len__(self):
        """
        Returns the total length of all favorite sets combined.
        """
        total_length = 0
        for desk in self.manager_regulation:
            total_length += len(desk.favorite_set)
        return total_length

    def __getitem__(self, index):
        """
        Returns the item at the specified index in the combined favorite sets.
        """
        count = 0
        for desk in self.manager_regulation:
            if count <= index < count + len(desk.favorite_set):
                inner_index = index - count
                return list(desk.favorite_set)[inner_index]
            count += len(desk.favorite_set)
        raise IndexError

    def __next__(self):
        """
        Raises a StopIteration exception.
        """
        raise StopIteration()
