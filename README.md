# Multi-Agent Retail Inventory Optimization System

![Ollama Logo](https://avatars.githubusercontent.com/u/141423365?s=200&v=4)

## 📌 Project Overview
This project leverages a multi-agent architecture integrated with local LLMs (Ollama) to optimize retail inventory management. Three autonomous agents—**StoreAgent**, **WarehouseAgent**, and **SupplierAgent**—collaborate to:

- Monitor sales trends and inventory levels
- Forecast demand and suggest pricing strategies
- Automate decision-making for reordering and supplier communication

The agents use structured data and dynamic prompts to interact with a locally hosted LLM (`phi` via Ollama) for context-aware retail decisions.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/multi-agent-inventory.git
cd multi-agent-inventory
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download Ollama and Run the Model
- Install [Ollama](https://ollama.com/)
- Pull the Phi model:
```bash
ollama run phi
```
- Keep Ollama running locally at `http://localhost:11434`

---

## 🚀 How to Run Agents

### Main File
```bash
python agents/main.py
```

### Store Agent
```bash
python agents/store_agent.py
```

### Warehouse Agent
```bash
python agents/warehouse_agent.py
```

### Supplier Agent
```bash
python agents/supplier_agent.py
```

You can simulate a particular day by modifying the `simulate_day(day_number)` function call.

---

## 🧠 Ollama Integration
The agents communicate with the local Ollama LLM via REST API. Each agent:

- Extracts daily data from CSV files
- Formats a natural language prompt
- Sends the prompt to the Ollama server (`phi` model)
- Parses the streaming NDJSON response for decision output

Example API call:
```python
response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi", "prompt": prompt},
    stream=True
)
```

---

## 📊 Example Output
```
[StoreAgent] Day 1 Decision:
Based on high sales volume and good customer reviews, consider a slight price increase and marketing promotion.

[WarehouseAgent] Day 1 Decision:
Stock levels are low and close to the reorder point. Reorder today to avoid stockouts.

[SupplierAgent] Day 1 Decision:
Prepare a shipment based on historical lead times and warehouse capacity. Ensure timely dispatch.
```

---


## 📬 Contact
**Dhanashri Patil**  
📧 ![Email](https://img.icons8.com/ios-filled/20/000000/email-open.png) patil.dhanashrik@gmail.com  
🐙 ![GitHub](https://img.icons8.com/ios-glyphs/20/000000/github.png) [DhanashriPatil11](https://github.com/DhanashriPatil11)  
🔗 ![LinkedIn](https://img.icons8.com/ios-filled/20/000000/linkedin.png) [dhanashri-patil24](https://www.linkedin.com/in/dhanashri-patil24/)

---

> This project was built as part of the Hackathon challenge: **Optimizing Retail Inventory with Multi Agents** 💡

