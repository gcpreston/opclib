import unittest

from opclib import opcutil


class TestOPCLib(unittest.TestCase):
    """
    Tests for ``opclib`` module.
    """

    valid_colors = ['#000000', '#123456', '#987abc', '#abcdef', '#ffffff']
    invalid_colors = ['#fffffg', 'fail', 'abcdef', '#abcdef0', '#abcde', '#abc']

    def test_is_color(self):
        for color in self.valid_colors:
            self.assertTrue(opcutil.is_color(color))

        for color in self.invalid_colors:
            self.assertFalse(opcutil.is_color(color))

    def test_is_color_list(self):
        self.assertFalse(
            opcutil.is_color_list(['#001122', '334455', '#667788']))
        self.assertFalse(opcutil.is_color_list([]))

        self.assertTrue(
            opcutil.is_color_list(['#001122', '#334455', '#667788']))
        self.assertTrue(opcutil.is_color_list(['#FA016B']))

    def test_get_color(self):
        for color in self.invalid_colors:
            with self.assertRaises(ValueError):
                # Please provide a color in the format '#RRGGBB'.
                opcutil.get_color(color)

        self.assertEqual(opcutil.get_color('#000000'), (0, 0, 0))
        self.assertEqual(opcutil.get_color('#0eff32'), (14, 255, 50))

    def test_even_spread(self):
        with self.assertRaises(ValueError):
            # no colors provided
            opcutil.even_spread([], 5)
        with self.assertRaises(ValueError):
            # cannot spread across a negative number of LEDs
            opcutil.even_spread(['c1', 'c2'], -3)

        self.assertEqual(opcutil.even_spread(['c1', 'c2', 'c3'], 9),
                         ['c1', 'c1', 'c1',
                          'c2', 'c2', 'c2',
                          'c3', 'c3', 'c3'])
        self.assertEqual(opcutil.even_spread(['c1', 'c2', 'c3'], 10),
                         ['c1', 'c1', 'c1', 'c1',
                          'c2', 'c2', 'c2',
                          'c3', 'c3', 'c3'])
        self.assertEqual(opcutil.even_spread(['c1', 'c2', 'c3'], 11),
                         ['c1', 'c1', 'c1', 'c1',
                          'c2', 'c2', 'c2', 'c2',
                          'c3', 'c3', 'c3'])
        self.assertEqual(opcutil.even_spread(['c1'], 0), [])
        self.assertEqual(opcutil.even_spread(['c1'], 5),
                         ['c1', 'c1', 'c1', 'c1', 'c1'])

    def test_spread(self):
        with self.assertRaises(ValueError):
            # no values provided
            opcutil.spread([], 2, 6)
        with self.assertRaises(ValueError):
            # list length cannot be negative
            opcutil.spread(['c1', 'c2'], 1, -3)
        with self.assertRaises(ValueError):
            # sequence length cannot be negative
            opcutil.spread(['c1', 'c2'], -2, 6)

        self.assertEqual(opcutil.spread(['c1'], 2, 5),
                         ['c1', 'c1', 'c1', 'c1', 'c1'])
        self.assertEqual(opcutil.spread(['c1', 'c2'], 2, 8),
                         ['c1', 'c1',
                          'c2', 'c2',
                          'c1', 'c1',
                          'c2', 'c2'])
        self.assertEqual(opcutil.spread(['c1', 'c2', 'c3'], 3, 7),
                         ['c1', 'c1', 'c1',
                          'c2', 'c2', 'c2',
                          'c3'])

    def test_shift(self):
        self.assertEqual(opcutil.shift((0, 0, 0), (100, 100, 100), 0.1),
                         (10, 10, 10))
        self.assertEqual(opcutil.shift((0, 50, 100), (100, 100, 100), 0.5),
                         (50, 75, 100))
        self.assertEqual(opcutil.shift((0, 0, 0), (100, 100, 100), 1.2),
                         (120, 120, 120))
        self.assertEqual(opcutil.shift((0, 0, 0), (100, 100, 100), -0.5),
                         (-50, -50, -50))

    def test_rotate_left(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(opcutil.rotate_left(nums, 0), nums)
        self.assertEqual(opcutil.rotate_left(nums, 1), [2, 3, 4, 1])
        self.assertEqual(opcutil.rotate_left(nums, -1), [4, 1, 2, 3])
        self.assertEqual(opcutil.rotate_left(nums, 2),
                         opcutil.rotate_left(nums, -2))
        self.assertEqual(opcutil.rotate_left(nums, 5),
                         opcutil.rotate_left(nums, 1))

    def test_rotate_right(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(opcutil.rotate_right(nums, 0), nums)
        self.assertEqual(opcutil.rotate_right(nums, 1), [4, 1, 2, 3])
        self.assertEqual(opcutil.rotate_right(nums, -1), [2, 3, 4, 1])
        self.assertEqual(opcutil.rotate_left(nums, 2),
                         opcutil.rotate_left(nums, -2))
        self.assertEqual(opcutil.rotate_right(nums, 5),
                         opcutil.rotate_right(nums, 1))


if __name__ == '__main__':
    unittest.main()
