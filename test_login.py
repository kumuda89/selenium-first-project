from POMpages.loginpage import LoginPage
def test_login(set_tear):
    login=LoginPage(set_tear)
    login.login()