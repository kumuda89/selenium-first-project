from POMpages.Address import NewAddress
def test_cart(login):
    add=NewAddress(login)
    add.add()