from abc import ABC, abstractmethod


class Post(ABC):

    @abstractmethod
    def __init__(self, owner):
        self._owner = owner  # The user who published the post

    # Returns the user who published the post
    def get_owner(self):
        return self._owner

    # Notifies the owner that a given user liked his post
    def like(self, user):
        if user != self._owner:
            self._owner.update_notifications(f"{user.get_username()} liked your post")
            print(f"notification to {self._owner.get_username()}: {user.get_username()} liked your post")

    # Notifies the owner that a given user commented on his post
    def comment(self, user, text):
        if user != self._owner:
            self._owner.update_notifications(f"{user.get_username()} commented on your post")
            print(f"notification to {self._owner.get_username()}: {user.get_username()} commented on your post: {text}")
