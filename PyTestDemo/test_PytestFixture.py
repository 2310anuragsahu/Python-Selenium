import pytest


@pytest.fixture()
def setup():
    print("Setup method: Once before every method")


def test_loginByEmail(setup):
    print("Login by Email")


# For below 2 methods, setup method will not run
# as we didn't give 'setup' in parenthesis
def test_loginByFaceBook():
    print("Login by Facebook")


def test_loginByTwitter():
    print("Login by Twitter")
