from .abstract_desk import AbstractDesk


class JournalDesk(AbstractDesk):
    def __init__(self, height, width, length, has_vase, max_weight_capacity):
        super().__init__(height, width, length)
        self.has_vase = has_vase
        self.max_weight_capacity = max_weight_capacity

    def __str__(self):
        return f"{super().__str__()}, has_vase={self.has_vase}, max_weight_capacity={self.max_weight_capacity}"
