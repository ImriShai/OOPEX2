""" This class is part of the observer design pattern and is also a singleton.
    The purpose of this class is to notify all the followers of a certain user about a new post. """


class FollowersNotifications:
    __instance = None

    def __init__(self):
        if FollowersNotifications.__instance is not None:
            raise Exception("Can only initialize one singleton")
        self.__userFollowers = {}  # Maps a user to his followers

    @staticmethod
    def get_instance():
        if FollowersNotifications.__instance is None:
            FollowersNotifications.__instance = FollowersNotifications()
            return FollowersNotifications.__instance
        return FollowersNotifications.__instance

    def subscribe(self, user, follower):
        if user not in self.__userFollowers:
            self.__userFollowers[user] = []
        self.__userFollowers[user].append(follower)

    def unsubscribe(self, user, follower):
        self.__userFollowers[user].remove(follower)

    # Notify all of user's followers about a new post
    def notify(self, user):
        for follower in self.__userFollowers[user]:
            follower.update_notifications(f"{user.get_username()} has a new post")
