import pytest


@pytest.yield_fixture()
def setup():
    print("Once Before every method")
    yield
    print("Once After every method")


def test_loginByEmail(setup):
    print("Login by Email")


# For below 2 methods, setup method will not run
# as we didn't give 'setup' in parenthesis
def test_loginByFaceBook():
    print("Login by Facebook")


def test_loginByTwitter():
    print("Login by Twitter")
