class WritingDesk:
    instance = None

    def __init__(self, number_of_drawers=2, has_keyboard_tray=False, max_weight_capacity=85, current_height=70, max_height=74):
        self.number_of_drawers = number_of_drawers
        self.has_keyboard_tray = has_keyboard_tray
        self.max_weight_capacity = max_weight_capacity
        self.current_height = current_height
        self.max_height = max_height

    def adjustHeight(self, centimeters):
        new_height = self.current_height + centimeters
        if new_height <= self.max_height:
            self.current_height = new_height

    def moveDown(self, centimeters):
        new_height = self.current_height - centimeters
        if new_height >= 0:
            self.current_height = new_height

    @staticmethod
    def getInstance():
        if not WritingDesk.instance:
            WritingDesk.instance = WritingDesk()
        return WritingDesk.instance

    def __str__(self):
        return f"WritingDesk(number_of_drawers={self.number_of_drawers}, " \
               f"has_keyboard_tray={self.has_keyboard_tray}, " \
               f"max_weight_capacity={self.max_weight_capacity}, " \
               f"current_height={self.current_height}, " \
               f"max_height={self.max_height})"