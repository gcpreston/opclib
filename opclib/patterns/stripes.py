from typing import List
from ..opcutil import ColorHex, ColorData, get_color, spread
from ..interface import StaticLightConfig


class Stripes(StaticLightConfig):
    """
    Display multiple static colors.
    """

    def __init__(self, colors: List[ColorHex], num_leds: int = 512):
        super().__init__(num_leds)
        self.colors = [get_color(c) for c in colors]

    def pattern(self) -> List[ColorData]:
        return spread(self.colors, 10, self.num_leds)
