class FollowersNotifications:

    def __init__(self):
        self.userFollowers = {}

    def subscribe(self, user, follower):
        self.userFollowers[user].add(follower)

    def unsubscribe(self, user, follower):
        self.userFollowers[user].remove(follower)

    def notify(self, user):
        for follower in self.userFollowers[user]:
            follower.notify()
