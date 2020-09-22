import os

class Archive():
    def __init__(self, name, path):
        self.path = path
        self.name = name

        self.stale_size = 0

    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def get_stale_size(self):
        file = self.path + '/' + self.name if self.path != '' else self.name
        return os.path.getsize(file)