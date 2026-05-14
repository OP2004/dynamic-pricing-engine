import matplotlib.pyplot as plt
import os

def generate_price_chart(current_price, competitor_price):

    labels = ["Competitor Price", "AI Price"]
    values = [competitor_price, current_price]

    plt.figure(figsize=(5,3))
    plt.bar(labels, values, color=["red", "green"])
    plt.title("Price Comparison")

    file_path = os.path.join(os.path.dirname(__file__), "price_chart.png")

    plt.savefig(file_path)
    plt.close()

    return file_path