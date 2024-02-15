from SocialNetworkProj.Posts.TextPost import TextPost
from SocialNetworkProj.Posts.ImagePost import ImagePost
from SocialNetworkProj.Posts.SalePost import SalePost

""" This class follows the factory design pattern in order to construct posts of different types. """


class PostFactory:

    @staticmethod
    def create_post(post_type, owner, args):
        if post_type == "Text":
            return TextPost(owner, *args)
        if post_type == "Image":
            return ImagePost(owner, *args)
        if post_type == "Sale":
            return SalePost(owner, *args)
        raise Exception(f"Post type: {post_type} is not a supported post type")
