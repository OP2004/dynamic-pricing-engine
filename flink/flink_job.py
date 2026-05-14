from pyflink.datastream import StreamExecutionEnvironment


def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    # Sample stream to demonstrate Flink processing
    data_stream = env.from_collection([
        "Product=Mobile, UnitsSold=120",
        "Product=Laptop, UnitsSold=35",
        "Product=Shoes, UnitsSold=95"
    ])

    # Print all events
    data_stream.print()

    env.execute("Dynamic Pricing Flink Job")


if __name__ == "__main__":
    main()