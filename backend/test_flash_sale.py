from pricing_logic import apply_flash_sale_adjustment

price = 1000
units_sold = 100  # High demand

new_price = apply_flash_sale_adjustment(price, units_sold)

print("Original Price:", price)
print("New Price:", new_price)