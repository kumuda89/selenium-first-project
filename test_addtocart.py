from POMpages.cart import Addtocart
def test_cart(login):
    cart=Addtocart(login)
    cart.cart()