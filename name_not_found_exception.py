class NameNotFoundException(Exception):
    def __init__(self, name, message=f'Flavor not found in list of '
                                     f'available flavors'):
        self.name = name
        self.message = message
        super().__init__(self.message)
