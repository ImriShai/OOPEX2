from SocialNetworkProj.FollowersNotifications import FollowersNotifications
from SocialNetworkProj.Posts.PostFactory import PostFactory


class User:

    def __init__(self, username, password):
        self.__online = True  # True iff the user is logged in
        self.__username = username
        self.__password = password
        self.__numPosts = 0
        self.__numFollowers = 0
        self.__following = []  # A list of users this user is following
        self.__notifications = []
        self.__followerNotifications = FollowersNotifications.get_instance()

    def set_online(self, status):
        if status == self.__online:
            if status:
                raise Exception(f"{self.__username} is already online")
            raise Exception(f"{self.__username} is already offline")
        self.__online = status

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def __add_follower(self):
        self.__numFollowers += 1

    def __remove_follower(self):
        self.__numFollowers -= 1

    # =====================

    def follow(self, user):
        if not self.__online:
            raise Exception("User must be online!")
        if user in self.__following:
            raise Exception("You are already following this user!")
        self.__following.append(user)
        user.__add_follower()
        self.__followerNotifications.subscribe(user, self)
        print(f"{self.__username} started following {user.get_username()}")

    def unfollow(self, user):
        if not self.__online:
            raise Exception("User must be online!")
        if user not in self.__following:
            raise Exception("In order to unfollow you must follow first!")
        self.__following.remove(user)
        user.__remove_follower()
        self.__followerNotifications.unsubscribe(user, self)
        print(f"{self.__username} unfollowed {user.get_username()}")

    def publish_post(self, post_type, *args):
        if not self.__online:
            raise Exception("User must be online!")
        self.__numPosts += 1
        post = PostFactory.create_post(post_type, self, args)
        self.__followerNotifications.notify(self)
        print(post)
        return post

    def print_notifications(self):
        if not self.__online:
            raise Exception("User must be online!")
        print(f"{self.__username}'s notifications:")
        for notification in self.__notifications:
            print(notification)

    # add a new notification to the notifications list
    def update_notifications(self, notification):
        self.__notifications.append(notification)

    def __str__(self):
        res = f"User name: {self.__username}, Number of posts: {self.__numPosts}, Number of followers: {self.__numFollowers}"
        return res
