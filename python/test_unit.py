import unittest

'''
    Python standard library unittest
    https://docs.python.org/3/library/unittest.html
'''


def add_one(x):
    return x + 1


def square(x):
    return x * x


class TestMathFunc(unittest.TestCase):  # Subclass unittest.TestCase to create a test case
    # Each test function's name should start as "test".
    # This naming convention informs the test runner about which methods are tests.
    def test_add_one(self):
        self.assertEqual(add_one(3), 4)         # check doc for more assert methods

    def test_square(self):
        self.assertEqual(square(2), 4)

    @unittest.skip("demonstrating skipping")    # Note: you can skip class as well, check doc for more decorators
    def test_condition(self):
        self.assertTrue(3 > 1)
        self.assertFalse(10 < 2)

    def test_even(self):
        # Use the subTest() context manager to distinguish small differences among your tests.
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

        # Without using subtest, execution will stop after the first failure
        # for i in range(0, 6):
        #     self.assertEqual(i % 2, 0)


class TestStringMethods(unittest.TestCase):
    # setUp() will be automatically called for every single test we run
    def setUp(self):
        self.test_string = 'hello world'

    # if setUp() succeeded, tearDown() will be run whether the test method succeeded or not.
    def tearDown(self):
        self.test_string = None

    def test_split(self):
        self.assertEqual(self.test_string.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            self.test_string.split(2)  # Must be str, not int


if __name__ == "__main__":
    '''
    Command line interface
    
    $ python -m unitest test_unit   # test discovery, filename should follow naming convention
    $ python -m unitest test_unit
    $ python -m unitest test_unit.TestMathFunc
    $ python -m unitest test_unit.TestMathFunc.test_square
    
    try -v option to show more detailed 
    $ python -m unittest -h for more options
    
    '''
    unittest.main()
