def build_features(
    units_sold,
    inventory,
    competitor_price,
    category_encoded
):

    # 1. Demand pressure (how fast product is selling)
    demand_pressure = units_sold / (inventory + 1)

    # 2. Inventory scarcity (low stock = higher price power)
    inventory_pressure = 1 / (inventory + 1)

    # 3. Price advantage (how cheap/expensive vs market)
    price_advantage = competitor_price * 0.05

    # 4. Category weight (simple business bias)
    category_weight = category_encoded * 0.1

    return [
        demand_pressure,
        inventory_pressure,
        price_advantage,
        category_weight
    ]