import unittest
from RegressionTesting.Package1.TC_LoginTest import LoginTest
from RegressionTesting.Package1.TC_SignUpTest import SignUpTest
from RegressionTesting.Package2.TC_PaymentTest import PaymentTest
from RegressionTesting.Package2.TC_PaymentReturnsTest import PaymentReturnsTest


TC1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
TC2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
TC3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
TC4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

sanityTestSuite = unittest.TestSuite([TC1, TC2])
functionalTestSuite = unittest.TestSuite([TC3, TC4])
masterTestSuite = unittest.TestSuite([TC1, TC2, TC3, TC4])


unittest.TextTestRunner().run(masterTestSuite)
