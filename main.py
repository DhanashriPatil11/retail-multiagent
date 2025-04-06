# main.py
from agents.store_agent import StoreAgent
from agents.warehouse_agent import WarehouseAgent
from agents.supplier_agent import SupplierAgent

def run_simulation():
    store = StoreAgent()
    warehouse = WarehouseAgent()
    supplier = SupplierAgent()

    for day in range(5):  # Adjust based on your data length
        print(f"\n--- Simulation Day {day + 1} ---")
        store.simulate_day(day)
        warehouse.simulate_day(day)
        supplier.simulate_day(day)

if __name__ == "__main__":
    run_simulation()
