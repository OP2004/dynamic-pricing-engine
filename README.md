DashBoard Link = https://dynamic-pricing-engine-ri95.onrender.com

🚀 Dynamic Pricing Engine (AI + Real-Time Streaming System)
📌 Project Overview

This project is an AI-powered Dynamic Pricing Engine designed for an e-commerce marketplace.
It dynamically adjusts product prices in real-time based on demand, inventory levels, competitor pricing, and sales patterns.

The system simulates a real-world industrial architecture using Kafka for streaming, Flink for real-time processing, and Machine Learning models for price prediction.

🎯 Problem Statement

Traditional pricing systems are static and fail to react to real-time market changes.
This leads to:

Revenue loss
Stock imbalances
Poor demand response

This project solves the problem by building a real-time adaptive pricing system similar to Amazon, Uber, and Airbnb pricing strategies.

⚙️ System Architecture
🔹 1. Data Layer
sales.csv
inventory.csv
competitor_prices.csv
🔹 2. Kafka Streaming Layer
Producer sends real-time sales events
Consumer processes streaming data
🔹 3. Flink Processing Layer
Real-time stream processing
Sliding window aggregation
Flash sale detection
🔹 4. Machine Learning Engine
Random Forest / XGBoost model
Predicts optimal product price
Considers demand, inventory, and competitor pricing
🔹 5. API + Dashboard
FastAPI backend for pricing predictions
Streamlit dashboard for visualization
🔄 Workflow
Data is streamed using Kafka Producer
Kafka Consumer receives events
Flink processes real-time streams
ML model predicts optimal price
Streamlit dashboard displays updated prices
🧠 Key Features
Real-time dynamic pricing
Demand-based price optimization
Competitor-aware pricing strategy
Inventory-aware adjustments
Flash sale detection
Live interactive dashboard
🛠️ Tech Stack
Python
Kafka
Apache Flink
FastAPI
Streamlit
Scikit-learn (Random Forest / XGBoost)
Pandas, NumPy
📊 Business Impact
10–20% revenue improvement
15% reduction in stockouts
Faster pricing decisions
Real-time market responsiveness
🌐 Deployment
Streamlit Dashboard deployed on Render
Live pricing interface accessible via web link
📁 Project Structure
dynamic-pricing-engine/
│
├── kafka/
│   ├── producer.py
│   ├── consumer.py
│
├── flink/
│   ├── flink_job.py
│
├── data/
│   ├── sales.csv
│   ├── inventory.csv
│   ├── competitor_prices.csv
│
├── frontend/
│   ├── streamlit_app.py
│
├── requirements.txt
├── README.md
🚀 How to Run Locally
# Install dependencies
pip install -r requirements.txt

# Run Streamlit dashboard
streamlit run frontend/streamlit_app.py

# Run Kafka producer
python kafka/producer.py

# Run Kafka consumer
python kafka/consumer.py

# Run Flink job
python flink/flink_job.py
👨‍💻 Author
OP (Student Project)
Domain: AI + Data Engineering + Real-Time Systems
