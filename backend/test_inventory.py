from pricing_logic import apply_inventory_adjustment

price = 1000

print("Low stock (5):", apply_inventory_adjustment(price, 5))
print("Normal stock (100):", apply_inventory_adjustment(price, 100))
print("Excess stock (700):", apply_inventory_adjustment(price, 700))