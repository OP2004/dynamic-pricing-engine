def apply_flash_sale_adjustment(price, units_sold):
    if units_sold > 80:
        price *= 1.15
    return price


def apply_inventory_adjustment(price, stock):
    if stock < 10:
        price *= 1.20
    elif stock > 500:
        price *= 0.90
    return price


def blend_with_competitor_price(ml_price, competitor_price):
    final_price = (ml_price * 0.70) + (competitor_price * 0.30)
    return final_price