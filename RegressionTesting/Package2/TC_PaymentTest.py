import unittest


class PaymentTest(unittest.TestCase):
    def test_paymentInDollar(self):
        print("Payment in Dollar")
        self.assertTrue(True)

    def test_paymentInRupees(self):
        print("Payment in Rupees")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()