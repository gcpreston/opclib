from ..interface import StaticLightConfig
from ..opcutil import Color, get_color


class SolidColor(StaticLightConfig):
    """
    Display a solid color.
    """

    def __init__(self, color: str, num_leds: int = 512):
        """
        Initialize a new SolidColor configuration.
        :param color: the color to dislpay (in format "#RRGGBB")
        """
        super().__init__(num_leds)
        self.color: Color = get_color(color)

    def pattern(self):
        return [self.color] * self.num_leds
