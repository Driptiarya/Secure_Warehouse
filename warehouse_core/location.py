from abc import ABC, abstractmethod
import os

# =====================================================================
# [OOP CONCEPT 1: COMPOSITION ('HAS-A' RELATIONSHIP)]
# Location represents physical warehouse positioning. BaseProduct HAS-A Location.
# Decouples spatial layout tracking from pricing and stock rules.
# =====================================================================
class Location:
    def __init__(self, rack: str):
        self.rack = rack

# =====================================================================
# [OOP CONCEPT 2: ABSTRACTION & ENCAPSULATION]
# BaseProduct is an Abstract Base Class (ABC). It enforces a contract:
# all products MUST implement calc_fee(). It also encapsulates protected _stock.
# =====================================================================
class BaseProduct(ABC):
    def __init__(self, name: str, price: float, rack: str):
        self.name = name
        self.price = price
        self.loc = Location(rack)     # [COMPOSITION IN ACTION]
        self._stock = 10              # [ENCAPSULATION: Protected attribute]

    @property
    def stock(self) -> int:
        return self._stock            # Safe read-only getter

    def dispatch(self, qty: int) -> bool:
        # Invariant check: dispatch cannot exceed stock or be non-positive
        if qty <= 0 or qty > self._stock:
            raise ValueError(f'[Alert] Invalid dispatch ({qty}). Stock: {self._stock}')
        self._stock -= qty
        return True

    @abstractmethod
    def calc_fee(self, days: int) -> float:
        pass
