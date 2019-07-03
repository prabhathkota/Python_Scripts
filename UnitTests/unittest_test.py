"""
setup()
    This is called immediately before calling the test method
teardown()
    Method called immediately after the test method has been called and the result recorded
"""
import unittest


class FooTest(unittest.TestCase):
    """Sample test case"""

    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print("---FooTest:setUp_:begin")

        testName = self.shortDescription()
        if (testName == "Test routine A"):
            print("setting up for test A")

        elif (testName == "Test routine B"):
            print("setting up for test B")

        else:
            print("UNKNOWN TEST ROUTINE")

        print("FooTest:setUp_:end")

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print("---FooTest:tearDown_:begin")

        testName = self.shortDescription()
        if (testName == "Test routine A"):
            print("cleaning up after test A")

        elif (testName == "Test routine B"):
            print("cleaning up after test B")

        else:
            print("UNKNOWN TEST ROUTINE")

        print("FooTest:tearDown_:end")

    def testA(self):
        """Test routine A"""
        print("Running test A")

    def testB(self):
        """Test routine B"""
        print("Running test B")


if __name__ == "__main__":
    unittest.main()
    # creating a new test suite
    newSuite = unittest.TestSuite()

    # adding a test case
    newSuite.addTest(unittest.makeSuite(FooTest))

