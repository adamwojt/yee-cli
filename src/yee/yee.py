import random

from webcolors import CSS3_NAMES_TO_HEX as COLOR_NAMES
from webcolors import name_to_rgb
from yeelight import Bulb, discover_bulbs


class Room:
    def __init__(self, bulb_ips):
        self.bulbs = [Bulb(ip) for ip in bulb_ips]

    def _execute_on_all_bulbs(self, method_name, *args, **kwargs):
        for bulb in self.bulbs:
            getattr(bulb, method_name)(*args, **kwargs)

    def toggle(self):
        self._execute_on_all_bulbs("toggle")

    def dim(self, level):
        self._execute_on_all_bulbs("set_brightness", level)

    def color(self, color_name):
        rgb = name_to_rgb(color_name)
        self._execute_on_all_bulbs("set_rgb", *rgb)

    def random_color(self):
        self.color(random.choice(list(COLOR_NAMES)))

    def on(self):
        self._execute_on_all_bulbs("turn_on")

    def off(self):
        self._execute_on_all_bulbs("turn_off")
