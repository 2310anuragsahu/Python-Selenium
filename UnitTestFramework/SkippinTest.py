import unittest


class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_testCase1(self):
        print("Test Case 1")

    @unittest.skip("this method is not ready")
    def test_testCase2(self):
        print("Test Case 2")

    # is the method not ready
    boolean = True

    @unittest.skipIf(boolean == True, "this method is not yet ready")
    def test_testCase3(self):
        print("Test Case 3")

    @unittest.expectedFailure
    def test_testCase4(self):
        print("Test Case 4")

    def test_testCase5(self):
        print("Test Case 5")

    def test_testCase6(self):
        print("Test Case 6")


if __name__ == "__main__":
    unittest.main()
