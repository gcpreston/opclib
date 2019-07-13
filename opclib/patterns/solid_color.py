from ..interface import StaticLightConfig
from ..opcutil import ColorHex, ColorData, get_color


class SolidColor(StaticLightConfig):
    """
    Display a solid color.
    """

    def __init__(self, color: ColorHex, num_leds: int = 512):
        """
        Initialize a new SolidColor configuration.
        :param color: the color to dislpay (in format "#RRGGBB")
        """
        super().__init__(num_leds)
        self.color: ColorData = get_color(color)

    def pattern(self):
        return [self.color] * self.num_leds
