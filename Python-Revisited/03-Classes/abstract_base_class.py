from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass

# ABC : Abstract Base Class
# Abstract Class cannot be instantiated


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from memory stream")


stream = MemoryStream()
stream.read()
