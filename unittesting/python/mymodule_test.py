#!/usr/bin/python
import unittest
import mymodule


class TestGlobalFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testadd(self):
        """1 and 2 is 3"""
        x = mymodule.add(1,2)
        self.assertEqual(x, 3)

    def testadd_types(self):
        """Different types raise exception"""
        x = mymodule.add(1, None)
        self.assertRaises(Exception)


if __name__ == '__main__':
    unittest.main(verbosity=2)


