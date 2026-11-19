from abc import ABC, abstractmethod
import os
from warehouse_core.products import TechItem, FreshItem
def main():
    api_key = os.getenv('WAREHOUSE_API_KEY', 'FALLBACK_DEV_KEY_SECURE')
    print(f'=== WAREHOUSE IMS (Auth: {api_key[:4]}****) ===')

    inventory = [
        TechItem('Laptop', 999.0, 'Aisle A-1'),
        FreshItem('Organic Milk', 4.0, 'Cold-Room B')
    ]
    print('\n--- WAREHOUSE STORAGE FEE INVENTORY REPORT ---')
    for item in inventory:
        # Polymorphism dynamically triggers correct calc_fee!
        fee = item.calc_fee(days=3)
        print(f'[{item.name}] Rack: {item.loc.rack} | 3-Day Holding Fee: ${fee:.2f}')

if __name__ == '__main__':
    main()