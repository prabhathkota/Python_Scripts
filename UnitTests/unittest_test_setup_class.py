"""
setup()
    This is called immediately before calling the test method
teardown()
    Method called immediately after the test method has been called and the result recorded

setUpClass(cls):
    A class method called before tests in an individual class are run
tearDownClass(cls):
    A class method called after tests in an individual class have run
"""
import unittest


class ExampleA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass in A\n")

    def setUp(self):
        print("setUp in A")

    def test1(self):
        print("test1 in A")

    def test2(self):
        print("test2 in A")

    def tearDown(self):
        print("tearDown in A")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass in A\n")


class ExampleB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass in B\n")

    def setUp(self):
        print("setUp in B")

    def test1(self):
        print("test1 in B")

    def test2(self):
        print("test2 in B")

    def tearDown(self):
        print("tearDown in B")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass in B\n")


if __name__ == "__main__":
    unittest.main()

    # creating a new test suite
    newSuite = unittest.TestSuite()

    # adding a test case
    newSuite.addTest(unittest.makeSuite(ExampleA))
    newSuite.addTest(unittest.makeSuite(ExampleB))

