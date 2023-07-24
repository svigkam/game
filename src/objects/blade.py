from src.config import *


class Blade:
    def __init__(self):
        self.damage = BLADE_BASE_POWER
        self.is_venom = False
        self.is_power = False
        self.timer = 5

    def get_blade_power(self) -> int:
        return self.damage + \
            (BLADE_VENOM_BAFF if self.is_venom else 0) + \
            (BLADE_POWER_BAFF if self.is_power else 0)
