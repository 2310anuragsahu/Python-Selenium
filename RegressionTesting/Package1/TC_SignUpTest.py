import unittest


class SignUpTest(unittest.TestCase):
    def test_signByEmail(self):
        print("SignUp by Email")
        self.assertTrue(True)

    def test_signByFaceBook(self):
        print("SignUp by Facebook")
        self.assertTrue(True)

    def test_signByTwitter(self):
        print("SignUp by Twitter")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()