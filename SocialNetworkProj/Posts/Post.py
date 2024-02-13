class Post:

    def __init__(self, owner):
        self._owner = owner

    def get_owner(self):
        return self._owner

    def like(self, user):
        self._owner.update_notifications(f"{user.get_username()} liked your post")

    def comment(self, user, text):
        self._owner.update_notifications(f"{user.get_username()} commented on your post: {text}")
