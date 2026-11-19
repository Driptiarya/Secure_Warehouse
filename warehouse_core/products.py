from warehouse_core.location import BaseProduct
# =====================================================================
# [OOP CONCEPT 3: INHERITANCE ('IS-A' RELATIONSHIP)]
# TechItem and FreshItem inherit attributes from BaseProduct for free
# and specialize their unique storage rate algorithms.
# =====================================================================
class TechItem(BaseProduct):
    def calc_fee(self, days: int) -> float:
        return days * 2.50  # Climate-controlled storage rate

class FreshItem(BaseProduct):
    def calc_fee(self, days: int) -> float:
        return days * 5.00  # Cold-chain refrigeration rate