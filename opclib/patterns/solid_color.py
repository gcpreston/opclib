from typing import List

from ..interface import StaticLightConfig
from ..opcutil import ColorHex, ColorData, get_color


class SolidColor(StaticLightConfig):
    """
    Display a solid color.
    """
    color: ColorData

    def __init__(self, color: ColorHex, num_leds: int = 512, **kwargs):
        """
        Initialize a new SolidColor configuration.
        :param color: the color to dislpay ("#RRGGBB" format)
        """
        super().__init__(num_leds, **kwargs)
        super().validate_color(color)
        self.color: ColorData = get_color(color)

    def pattern(self) -> List[ColorData]:
        return [self.color] * self.num_leds
