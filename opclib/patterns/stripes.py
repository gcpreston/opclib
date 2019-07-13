from typing import List
from .. import opcutil
from ..interface import Color, StaticLightConfig


class Stripes(StaticLightConfig):
    """
    Display multiple static colors.
    """

    def __init__(self, colors: List[str], num_leds: int = 512):
        super().__init__(num_leds)
        self.colors = [opcutil.get_color(c) for c in colors]

    def pattern(self) -> List[Color]:
        return opcutil.spread(self.colors, self.num_leds, 10)
