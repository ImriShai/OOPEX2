from SocialNetworkProj.User import User

""" This class follows the singleton design pattern and manages the network's users and their online status """


class SocialNetwork:
    __instance = None

    def __init__(self, name):
        if self.__instance is not None:
            raise Exception("Can only create one social network")
        self.__users = {}  # maps a username to the actual user instance
        self.__name = name
        print(f"The social network {self.__name} was created!")

    def __str__(self):
        result = f"{self.__name} social network:\n"
        for user in self.__users:
            result += f"{self.__users.get(user)}\n"
        return result

    @staticmethod
    def get_instance(name):
        if SocialNetwork.__instance is None:
            SocialNetwork.__instance = SocialNetwork(name)
            return SocialNetwork.__instance
        return SocialNetwork.__instance

    # Signs up a new user to the network and returns an instance of the new user.
    def sign_up(self, username, password):
        if username in self.__users:
            raise Exception("Username already exist!")
        if 4 > len(password) or len(password) > 8:
            raise Exception("Password doesn't meet the requirements")
        self.__users[username] = User(username, password)
        return self.__users[username]

    def log_in(self, username, password):
        if self.__users[username].get_password() != password:
            raise Exception("Wrong password")
        self.__users[username].set_online(True)
        print(f"{username} connected")

    def log_out(self, username):
        self.__users[username].set_online(False)
        print(f"{username} disconnected")
