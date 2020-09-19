import os

class Archive():
    def __init__(self, name, path):
        self.path = path
        self.name = name

        self.stale_size = None

    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_stale_size(self, size):
        self.stale_size = size

    def get_stale_size(self):
        return self.stale_size

    def get_size(self):
        file = self.path + '/' + self.name
        return os.path.getsize(file)