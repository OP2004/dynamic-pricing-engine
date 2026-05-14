from pricing_logic import blend_with_competitor_price

ml_price = 1000
competitor_price = 900

final_price = blend_with_competitor_price(ml_price, competitor_price)

print("ML Price:", ml_price)
print("Competitor Price:", competitor_price)
print("Final Blended Price:", final_price)