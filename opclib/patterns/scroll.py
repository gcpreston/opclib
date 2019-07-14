from typing import List
from ..interface import DynamicLightConfig
from ..opcutil import ColorData, get_color, spread, rotate_right


class Scroll(DynamicLightConfig):
    """
    Scroll through a multi-colored line.
    """
    color_list: List[ColorData]  # colors to scroll
    pixels: List[ColorData]  # current list of pixels
    speed = 8

    def __init__(self, color_list: List[str], speed: int = None,
                 num_leds: int = 512, **kwargs):
        """
        Initialize a new Scroll configuration.
        :param color_list: the colors to use ("#RRGGBB" format)
        """
        super().__init__(speed, num_leds, **kwargs)
        super().validate_color_list(color_list)

        self.color_list = [get_color(c) for c in color_list]
        self.pixels = spread(self.color_list, 10, self.num_leds)

    def __next__(self) -> List[ColorData]:
        self.pixels = rotate_right(self.pixels, 1)
        return self.pixels
