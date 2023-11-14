class NameNotFoundException(Exception):
    def __init__(self, message='Flavor not found in list of available flavors'):
        self.message = message
        super().__init__(self.message)
