import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import time
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Live Pricing Simulator",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Live Dynamic Pricing Engine (Streaming Simulator)")
st.markdown("Multi-product AI pricing with real-time simulation updates")

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Global Controls")

refresh_speed = st.sidebar.slider("Refresh Speed (sec)", 1, 10, 3)
num_products = st.sidebar.slider("Number of Products", 2, 10, 5)

st.sidebar.markdown("---")
st.sidebar.info("🔄 Auto-updating pricing simulation enabled")

# ---------------- PRODUCT GENERATION ----------------
def generate_products(n):
    products = []
    for i in range(n):
        products.append({
            "product": f"SKU-{1000+i}",
            "demand": random.randint(50, 500),
            "inventory": random.randint(20, 300),
            "competitor_price": random.randint(500, 2000),
            "season_factor": round(random.uniform(0.8, 1.5), 2)
        })
    return products

products = generate_products(num_products)

# ---------------- API ----------------
API_URL = "http://127.0.0.1:8000/predict"

def get_price(payload):
    try:
        r = requests.post(API_URL, json=payload, timeout=2)
        if r.status_code == 200:
            return r.json().get("recommended_price", None)
    except:
        return None

# ---------------- LIVE LOOP ----------------
placeholder = st.empty()

while True:
    df_rows = []

    total_revenue = 0

    for p in products:
        payload = {
            "demand": p["demand"],
            "inventory": p["inventory"],
            "competitor_price": p["competitor_price"],
            "season_factor": p["season_factor"],
            "customer_segment": "Medium Value"
        }

        recommended = get_price(payload)

        if not recommended:
            recommended = p["competitor_price"] * (1 + (p["demand"] - p["inventory"]) / 1000) * p["season_factor"]

        revenue = recommended * p["inventory"]
        total_revenue += revenue

        df_rows.append([
            p["product"],
            p["demand"],
            p["inventory"],
            p["competitor_price"],
            round(recommended, 2),
            round(revenue, 2)
        ])

    df = pd.DataFrame(df_rows, columns=[
        "Product", "Demand", "Inventory", "Competitor Price",
        "Recommended Price", "Est. Revenue"
    ])

    with placeholder.container():

        # ---------------- KPI ----------------
        col1, col2, col3 = st.columns(3)

        col1.metric("📦 Products", num_products)
        col2.metric("💰 Total Revenue", f"₹{total_revenue:,.0f}")
        col3.metric("⚡ Live Mode", "ACTIVE")

        st.markdown("---")

        # ---------------- TABLE ----------------
        st.subheader("📊 Multi-Product Pricing Table")
        st.dataframe(df, use_container_width=True)

        # ---------------- CHART ----------------
        st.subheader("📈 Revenue Distribution")

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df["Product"],
            y=df["Est. Revenue"],
            name="Revenue"
        ))

        st.plotly_chart(fig, use_container_width=True)

        st.info("🔄 Refreshing live simulation...")

    time.sleep(refresh_speed)
    st.rerun()