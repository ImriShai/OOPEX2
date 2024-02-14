from SocialNetworkProj.Posts.Post import Post
import matplotlib.pyplot as plt


class ImagePost(Post):

    def __init__(self, owner, image):
        super().__init__(owner)
        self.__image = image

    def display(self):
        plt.imshow(self.__image)

    def __str__(self):
        return f"{self.get_owner().get_username()} posted a picture\n"
