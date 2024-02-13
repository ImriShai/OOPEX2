from SocialNetworkProj.Posts.TextPost import TextPost
from SocialNetworkProj.Posts.ImagePost import ImagePost
from SocialNetworkProj.Posts.SalePost import SalePost


class PostFactory: # maybe static
    # __instance = None
    #
    # def __init__(self):
    #     pass
    #
    # @staticmethod
    # def get_instance():
    #     if PostFactory is None:
    #         PostFactory.__instance = PostFactory()
    #     return PostFactory.__instance

    @staticmethod
    def create_post(post_type, owner, args):
        if post_type == "Text":
            return TextPost(owner, *args)
        if post_type == "Image":
            return ImagePost(owner, *args)
        if post_type == "Sale":
            return SalePost(owner, *args)
        return None
