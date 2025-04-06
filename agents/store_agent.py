import json
import pandas as pd
import requests

class StoreAgent:
    def __init__(self):
        self.df = pd.read_csv("agents/data/pricing_optimization.csv")
        self.df.columns = self.df.columns.str.strip()

    def ask_ollama(self, prompt):
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "phi", "prompt": prompt},
            stream=True
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
                f"Sales Volume: {row['Sales Volume']}\n"
                f"Customer Reviews: {row['Customer Reviews']}\n"
                f"Return Rate (%): {row['Return Rate (%)']}%\n"
                f"Storage Cost: {row['Storage Cost']}\n"
                f"Elasticity Index: {row['Elasticity Index']}\n"
                "As a retail manager, should we promote this product, adjust pricing, or shift focus?"
            )
            result = self.ask_ollama(prompt)
            print(f"\n[StoreAgent] Day {day + 1} Decision:\n{result}")
        else:
            print(f"[StoreAgent] Day {day + 1}: No data available.")
