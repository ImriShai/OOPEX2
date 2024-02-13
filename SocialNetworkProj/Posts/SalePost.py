from SocialNetworkProj.Posts.Post import Post


class SalePost(Post):

    def __init__(self, owner, product_name, price, location):
        super().__init__(owner)
        self.__product_name = product_name
        self.__price = price
        self.__location = location
        self.__available = True

    def __str__(self):
        start = f"{self.get_owner().get_username()} posted a product for sale:\n"
        if self.__available:
            return start+f"For sale! {self.__product_name}, {self.__price:}, pickup from: {self.__location}"
        return start+f"Sold! {self.__product_name}, {self.__price:}, pickup from: {self.__location}"

    def sold(self, password):
        if self._owner.get_password() == password and self.__available:
            self.__available = False
            print(f"{self._owner.get_username()}'s product is sold")

    def discount(self, password, discount):
        if self._owner.get_password() == password and self.__available:
            self.__price *= (1 - (discount / 100))
            print(f"Discount on {self._owner.get_username()} product! the new price is {self.__price}")
