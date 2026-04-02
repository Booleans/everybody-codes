import re
from dataclasses import dataclass, field

pattern = r'^(\d{4}):([rR]{6}) ([gG]{6}) ([bB]{6})$'

@dataclass
class Scale:
    identfier: str
    red: str
    green: str
    blue: str
    shine: str = None
    red_value: int = field(init=False)
    green_value: int = field(init=False)
    blue_value: int = field(init=False)
    dominant_color: str = field(init=False)

    def __post_init__(self):
        self.red_value = int(self.red.replace('r', '0').replace('R', '1'), 2)
        self.green_value = int(self.green.replace('g', '0').replace('G', '1'), 2)
        self.blue_value = int(self.blue.replace('b', '0').replace('B', '1'), 2)
        self.dominant_color = max((self.red_value, 'red'), 
                                  (self.green_value, 'green'), 
                                  (self.blue_value, 'blue'))[1]


line = '2456:rrrrrr ggGgGG bbbbBB'

print(Scale('2456', 'rrRrrr', 'GGGGGG', 'BbBbBb'))
