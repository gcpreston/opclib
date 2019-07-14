from typing import List
from ..opcutil import ColorHex, ColorData, get_color, spread
from ..interface import StaticLightConfig


class Stripes(StaticLightConfig):
    """
    Display multiple static colors.
    """
    color_list: List[ColorData]  # colors to display

    def __init__(self, color_list: List[ColorHex], num_leds: int = 512,
                 **kwargs):
        """
        Initialize a new Stripes configuration.
        :param color_list: the colors to use ("#RRGGBB" format)
        """
        super().__init__(num_leds, **kwargs)
        super().validate_color_list(color_list)
        self.color_list = [get_color(c) for c in color_list]

    def pattern(self) -> List[ColorData]:
        return spread(self.color_list, 10, self.num_leds)
