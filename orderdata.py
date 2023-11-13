from dataclasses import dataclass


@dataclass(frozen=True)
class OrderData:
    type: str
    cash: int
    price: int
    ratio: int
