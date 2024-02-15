from SocialNetworkProj.Posts.Post import Post
from matplotlib import image as img, pyplot as plt


class ImagePost(Post):

    def __init__(self, owner, image):
        super().__init__(owner)
        self.__image = image

    # Displays the image on screen
    def display(self):
        image = img.imread(self.__image)
        plt.imshow(image)
        plt.show()
        print("Shows picture")

    def __str__(self):
        return f"{self.get_owner().get_username()} posted a picture\n"
