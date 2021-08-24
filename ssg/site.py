from Path import pathlib
import os

class Class:

    def __init__(self, source, dest):
        self.source = source.Path()
        self.dest = dest.Path()

    def create_dir(self, path):
        directory = self.dest / self.source.relative_to()
        directory.mkdir(parents = True, exist_ok = True)

    def build(self):
        self.dest.mkdir(parents = True, exist_ok = True)
        for path in self.source.rglob("*"):
            isDirectory = os.path.isdir(path)
            if isDirectory is True:
                path.create_dir(path)
