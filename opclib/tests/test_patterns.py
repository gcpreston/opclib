import unittest

from opclib.patterns import *


# -------------------------------
# Static configurations
# -------------------------------

class TestSolidColor(unittest.TestCase):
    """
    Tests for ``SolidColor`` pattern.
    """

    def test_pattern(self):
        self.assertRaises(TypeError, SolidColor, None)
        self.assertRaises(TypeError, SolidColor, 'bad color')
        self.assertRaises(TypeError, SolidColor, 'ABCDEF')

        sc1 = SolidColor('#ABCDEF')
        self.assertListEqual(sc1.pattern(), [(171, 205, 239)] * 512)

        sc2 = SolidColor('#abcdef', num_leds=16)
        self.assertListEqual(sc2.pattern(), [(171, 205, 239)] * 16)

        sc3 = SolidColor('#00FF16', num_leds=12)
        self.assertListEqual(sc3.pattern(), [(0, 255, 22)] * 12)

        sc4 = SolidColor('#00FF16', num_leds=-5)
        self.assertListEqual(sc4.pattern(), [])


class TestOff(unittest.TestCase):
    """
    Tests for ``Off`` pattern.
    """

    def test_pattern(self):
        off1 = Off()
        self.assertListEqual(off1.pattern(), [(0, 0, 0)] * 512)

        off2 = Off(num_leds=10)
        self.assertListEqual(off2.pattern(), [(0, 0, 0)] * 10)

        off3 = Off(num_leds=-2)
        self.assertListEqual(off3.pattern(), [])


class TestStripes(unittest.TestCase):
    """
    Tests for ``Stripes`` pattern.
    """

    def test_pattern(self):
        self.assertRaises(TypeError, Stripes, None)
        self.assertRaises(TypeError, Stripes, [])
        self.assertRaises(TypeError, Stripes, ['#001122', '334455', '#667788'])

        stripes1 = Stripes(['#001122', '#334455', '#667788'], num_leds=12)
        self.assertListEqual(stripes1.pattern(),
                             [*[(0, 17, 34)] * 4,
                              *[(51, 68, 85)] * 4,
                              *[(102, 119, 136)] * 4])

        stripes2 = Stripes(['#001122', '#334455', '#667788'], num_leds=13)
        self.assertListEqual(stripes2.pattern(),
                             [*[(0, 17, 34)] * 5,
                              *[(51, 68, 85)] * 4,
                              *[(102, 119, 136)] * 4])

        stripes3 = Stripes(['#001122', '#334455', '#667788'], num_leds=14)
        self.assertListEqual(stripes3.pattern(),
                             [*[(0, 17, 34)] * 5,
                              *[(51, 68, 85)] * 5,
                              *[(102, 119, 136)] * 4])

        stripes4 = Stripes(['#FFF000', '#000FFF'], width=3, num_leds=12)
        self.assertListEqual(stripes4.pattern(),
                             [*[(255, 240, 0)] * 3,
                              *[(0, 15, 255)] * 3] * 2)

        stripes5 = Stripes(['#FF0000', '#00FF00', '#0000FF'], width=4,
                           num_leds=6)
        self.assertListEqual(stripes5.pattern(),
                             [*[(255, 0, 0)] * 4,
                              *[(0, 255, 0)] * 2])

        stripes6 = Stripes(['#FF0000', '#00FF00', '#0000FF'], width=2,
                           num_leds=9)
        self.assertListEqual(stripes6.pattern(),
                             [*[(255, 0, 0)] * 2,
                              *[(0, 255, 0)] * 2,
                              *[(0, 0, 255)] * 2,
                              *[(255, 0, 0)] * 2,
                              (0, 255, 0)])


# -------------------------------
# Dyamic configurations
# -------------------------------

class TestFade(unittest.TestCase):
    """
    Tests for ```Fade``` configuration.
    """

    def test_next(self):
        self.assertRaises(TypeError, Fade, None)
        self.assertRaises(TypeError, Fade, [])
        self.assertRaises(TypeError, Fade, ['FF0000', '#00FF00', '#0000FF'])

        # I believe Fade does not work in the way I thought it did. Holding off
        # on writing more tests for this configuration until I have access to
        # a Fadecandy again, as I think a fade effect is automatically
        # implemented, so I could look into using that to simplify code.

        # fade1 = Fade(['#000000', '#640000'], num_leds=10)  # red: 0 -> 100
        # r = 0
        # for _ in range(10):
        #     self.assertListEqual(next(fade1), [(r, 0, 0)] * 10)
        #     r += 10


class TestScroll(unittest.TestCase):
    """
    Tests for ``Scroll`` configuration.
    """

    def test_next(self):
        self.assertRaises(TypeError, Scroll, None)
        self.assertRaises(TypeError, Scroll, [])
        self.assertRaises(TypeError, Scroll, ['FF0000', '#00FF00', '#0000FF'])

        scroll1 = Scroll(['#FF0000', '#00FF00', '#0000FF'], num_leds=6)
        self.assertListEqual(scroll1.pixels,
                             [(255, 0, 0), (255, 0, 0),
                              (0, 255, 0), (0, 255, 0),
                              (0, 0, 255), (0, 0, 255)])
        self.assertListEqual(next(scroll1),
                             [(0, 0, 255),
                              (255, 0, 0), (255, 0, 0),
                              (0, 255, 0), (0, 255, 0),
                              (0, 0, 255)])
        self.assertListEqual(next(scroll1),
                             [(0, 0, 255), (0, 0, 255),
                              (255, 0, 0), (255, 0, 0),
                              (0, 255, 0), (0, 255, 0)])
