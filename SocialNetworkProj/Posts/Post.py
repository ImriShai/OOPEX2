from abc import ABC, abstractmethod


class Post(ABC):

    @abstractmethod
    def __init__(self, owner):
        self._owner = owner

    def get_owner(self):
        return self._owner

    def like(self, user):
        if user != self._owner:
            self._owner.update_notifications(f"{user.get_username()} liked your post")
            print(f"notification to {self._owner.get_username()}: {user.get_username()} liked your post")

    def comment(self, user, text):
        if user != self._owner:
            self._owner.update_notifications(f"{user.get_username()} commented on your post")
            print(f"notification to {self._owner.get_username()}: {user.get_username()} commented on your post: {text}")
