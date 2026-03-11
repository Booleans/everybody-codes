import re
from dataclasses import dataclass, field


@dataclass
class Scale:
    identfier: str
    red: str
    green: str
    blue: str
    red_value: int = field(init=False)
    green_value: int = field(init=False)
    blue_value: int = field(init=False)
    dominant_color: str = field(init=False)

    def __post_init__(self):
        

pattern = 

line = '2456:rrrrrr ggGgGG bbbbBB'



print('hello world!')