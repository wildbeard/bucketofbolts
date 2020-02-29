from .Hardware import Hardware

class Bolt(Hardware):

    def __init__(self, hardware_type_id, hardware_size_id, user_id, name):
        super().__init__(hardware_type_id, hardware_size_id, user_id, name)
        self.__HARDWARE_TYPE = 1