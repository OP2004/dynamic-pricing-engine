from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

products = ["Shoes", "Watch", "Mobile", "Laptop", "TV"]

while True:
    event = {
        "product": random.choice(products),
        "units_sold": random.randint(1, 100),
        "inventory": random.randint(1, 500),
        "competitor_price": random.randint(1000, 80000)
    }

    producer.send("pricing-topic", event)
    producer.flush()

    print("Sent:", event)

    time.sleep(2)