

class Grid():

    def __init__(self, visible=True, value="0"):
        self.visible = visible
        self.value = value

    def set_status(self, status):
        self.visible = status

    def get_status(self):
        return self.visible

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value