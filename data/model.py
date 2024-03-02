from dataclasses import dataclass
from typing import final

@final
@dataclass
class Items:
    question: str
    answer: str
    topic: str


