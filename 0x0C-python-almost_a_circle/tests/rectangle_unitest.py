#!/usr/bin/python3
"""Rectangle function testing"""

import unittest
import rectangle


class TestRectangle(unittest.TestCase):

    def test_rectangle_output(self):
        """rectangle function output tester"""

        #self.assertAlmostEqual(rectangle(,))
    def test_rectangle_input(self):
        """rectangle func input tester"""

        self.assertRaises(TypeError, rectangle)