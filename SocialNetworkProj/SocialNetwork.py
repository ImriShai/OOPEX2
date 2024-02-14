from SocialNetworkProj.User import User


class SocialNetwork:
    __instance = None

    def __init__(self, name):
        if self.__instance is not None:
            raise Exception("Can only create one social network")
        self.passwords = {}
        self.users = {}
        self.name = name
        print(f"The social network {self.name} was created!")

    def __str__(self):
        result = f"{self.name} social network:\n"
        for user in self.users:
            result += f"{self.users.get(user)}\n"
        return result

    @staticmethod
    def get_instance(name):
        if SocialNetwork.__instance is None:
            SocialNetwork.__instance = SocialNetwork(name)
            return SocialNetwork.__instance
        return SocialNetwork.__instance

    def sign_up(self, username, password):
        if username in self.passwords:
            raise Exception("Username already exist!")
        if 4 > len(password) or len(password) > 8:
            raise Exception("Password doesn't meet the requirements")
        self.passwords[username] = password
        self.users[username] = User(username, password)
        return self.users[username]

    def log_in(self, username, password):
        if self.passwords[username] == password:
            self.users[username].set_online(True)
            print(f"{username} connected")

    def log_out(self, username):
        self.users[username].set_online(False)
        print(f"{username} disconnected")
