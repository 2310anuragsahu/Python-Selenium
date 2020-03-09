import unittest


def setUpModule():
    print("setUpModule")


def tearDownModule():
    print("tearDownModule")


class TestClass1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUp Class")

    @classmethod
    def tearDownClass(cls):
        print("tearDown Class")

    @classmethod
    def setUp(cls):
        print("setUp")

    @classmethod
    def tearDown(cls):
        print("tearDown")

    def test_testCase1(self):
        print("Test Case 1")

    def test_testCase2(self):
        print("Test Case 2")


class TestClass2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUp Class")

    @classmethod
    def tearDownClass(cls):
        print("tearDown Class")

    @classmethod
    def setUp(cls):
        print("setUp")

    @classmethod
    def tearDown(cls):
        print("tearDown")

    def test_testCase3(self):
        print("Test Case 3")

    def test_testCase4(self):
        print("Test Case 4")