from SocialNetworkProj.Posts.Post import Post


class TextPost(Post):

    def __init__(self, owner, text):
        super().__init__(owner)
        self.text = text

    def __str__(self):
        return f"{self.get_owner()} published a post:\n\"{self.text}\""
