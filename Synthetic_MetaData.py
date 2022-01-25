from enum import Enum
from dataclasses import dataclass
from typing import List, Optional
import numpy as np


class Segment:
    def __init__(self, d: int, b_low: float, b_high: float, m_low: int, m_high: int):
        self.b_low = b_low
        self.b_high = b_high
        self.coef_A = np.random.rand(d)
        self.coef_b = np.random.rand(1)
        self.m = np.random.randint(m_low, m_high)

    def generate_samples(self):
        samples = []
        for _ in range(self.m):
            x_sample = np.zeros(self.d)
            for i in range(self.d):
                x_sample[i] = np.random.RandomState.uniform(low=self.b_low[i], high=self.b_high[i], size=1)
            y = np.dot(x_sample, self.coef_A) + self.coef_b
            samples.append((x_sample, y))
        return samples






class Type(Enum):
    BINARY = 1
    CONTINUOUS = 2
    CATEGORICAL = 3


@dataclass
class MetaData:
    d: int
    segments: List[Segment]  # find how to define the boundaries
    type: Enum
    noise: int = 0

    @property
    def segments(self):
        return self.segments
