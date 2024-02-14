class FollowersNotifications:
    __instance = None

    def __init__(self):
        self.userFollowers = {}

    @staticmethod
    def get_instance():
        if FollowersNotifications.__instance is None:
            FollowersNotifications.__instance = FollowersNotifications()
            return FollowersNotifications.__instance
        return FollowersNotifications.__instance

    def subscribe(self, user, follower):
        if user not in self.userFollowers:
            self.userFollowers[user] = []
        self.userFollowers[user].append(follower)

    def unsubscribe(self, user, follower):
        self.userFollowers[user].remove(follower)

    def notify(self, user):
        for follower in self.userFollowers[user]:
            follower.update_notifications(f"{user.get_username()} has a new post")
