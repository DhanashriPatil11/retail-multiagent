import json
import pandas as pd
import requests

class SupplierAgent:
    def __init__(self):
        self.df = pd.read_csv("agents/data/inventory_monitoring.csv")
        self.df.columns = self.df.columns.str.strip()  # Clean column names

    def ask_ollama(self, prompt):
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "phi", "prompt": prompt},
            stream=True  # Important to stream the NDJSON
        )
        result = ""
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode("utf-8"))
                    result += data.get("response", "")
                except Exception as e:
                    print("Error parsing Ollama output:", e)
        return result.strip()

    def simulate_day(self, day):
        if day < len(self.df):
            row = self.df.iloc[day]
            prompt = (
                f"Product ID: {row['Product ID']}\n"
                f"Store ID: {row['Store ID']}\n"
                f"Stock Levels: {row['Stock Levels']}\n"
                f"Supplier Lead Time (days): {row['Supplier Lead Time (days)']}\n"
                f"Stockout Frequency: {row['Stockout Frequency']}\n"
                f"Reorder Point: {row['Reorder Point']}\n"
                f"Expiry Date: {row['Expiry Date']}\n"
                f"Warehouse Capacity: {row['Warehouse Capacity']}\n"
                f"Order Fulfillment Time (days): {row['Order Fulfillment Time (days)']}\n"
                "As a supplier, what actions should be taken today?"
            )
            result = self.ask_ollama(prompt)
            print(f"\n[SupplierAgent] Day {day + 1} Decision:\n{result}")
        else:
            print(f"[SupplierAgent] Day {day + 1}: No data available.")
