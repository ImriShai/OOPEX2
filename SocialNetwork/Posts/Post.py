from abc import ABC, abstractmethod


class Post(ABC):

    def __init__(self):
        pass

    def like(self, user):
        pass

    def comment(self, user, text):
        pass
