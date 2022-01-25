from enum import Enum
from dataclasses import dataclass
from typing import List
import numpy as np


class Segment:
    def __init__(self, d, b_low, b_high, m_low, m_high):
        self.b_low = b_low
        self.b_high = b_high
        self.coef_A = np.random.rand(d)
        self.coef_b = np.random.rand(1)
        self.m = np.random.randint(m_low, m_high)


class Type(Enum):
    BINARY = 1
    CONTINUOUS = 2


@dataclass
class MetaData:
    d: int
    segments: List[Segment]  # find how to define the boundaries
    noise: int = 0
    type = Enum
