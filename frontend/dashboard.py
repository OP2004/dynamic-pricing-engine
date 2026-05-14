import streamlit as st
import requests

st.set_page_config(page_title="Dynamic Pricing Engine", layout="wide")

st.title("🛒 AI Dynamic Pricing Engine (Real-Time System)")
st.markdown("Live competitor-aware ML pricing system")

# ---------------- INPUT ----------------
col1, col2 = st.columns(2)

with col1:
    category = st.selectbox("Category", ["Shoes", "Watch", "Mobile", "Laptop", "TV"])
    season = st.selectbox("Season", ["Summer", "Winter", "Festival"])
    customer_segment = st.selectbox("Customer Segment", ["Budget", "Standard", "Premium"])
    units_sold = st.number_input("Units Sold", min_value=0, value=20)
    inventory = st.number_input("Inventory Level", min_value=0, value=100)

# ---------------- FUNCTION: COMPETITOR API ----------------
def get_competitor_price(product):
    try:
        response = requests.get(
            "http://127.0.0.1:8001/competitor-price",
            params={"product": product}
        )
        data = response.json()

        if data["status"] == "success":
            return data["competitor_price"]
        else:
            return None
    except:
        return None


# ---------------- BUTTON ----------------
if st.button("🚀 Predict Optimal Price"):

    # STEP 1: get competitor price automatically
    competitor_price = get_competitor_price(category)

    if competitor_price is None:
        st.error("Failed to fetch competitor price")
        st.stop()

    st.info(f"Live Competitor Price: ₹{competitor_price}")

    # STEP 2: call ML API
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        params={
            "category": ["Shoes","Watch","Mobile","Laptop","TV"].index(category),
            "units_sold": units_sold,
            "season": ["Summer","Winter","Festival"].index(season),
            "customer_segment": ["Budget","Standard","Premium"].index(customer_segment),
            "inventory": inventory,
            "competitor_price": competitor_price
        }
    )

    result = response.json()

    # ---------------- SAFETY CHECK ----------------
    if result.get("status") != "success":
        st.error("Backend Error")
        st.write(result)
        st.stop()

    price = result["predicted_price"]
    chart = result["chart"]

    # ---------------- OUTPUT ----------------
    st.success(f"💰 Recommended Price: ₹{price:.2f}")

    col3, col4, col5 = st.columns(3)

    with col3:
        st.metric("Competitor Price", f"₹{competitor_price}")

    with col4:
        st.metric("AI Price", f"₹{price:.2f}")

    with col5:
        st.metric("Difference", f"₹{price - competitor_price:.2f}")

    # ---------------- CHART ----------------
    st.image(chart)

    # ---------------- INSIGHTS ----------------
    st.subheader("📊 Pricing Insights")

    if inventory < 20:
        st.warning("Low inventory → price increased")

    if price > competitor_price:
        st.info("Premium pricing applied")

    if price < competitor_price:
        st.info("Competitive pricing applied")

    if units_sold > 40:
        st.success("High demand detected")

    st.markdown("---")
    st.write("Real-time AI pricing system (Amazon-style architecture)")