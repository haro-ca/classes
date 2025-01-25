import pulsar

client = pulsar.Client("pulsar://localhost:6650")
consumer = client.subscribe("clases", subscription_name="shared-subscription")

batch = []
batch_size = 5

while True:
    msg = consumer.receive()
    try:
        batch.append(msg.data().decode("utf-8"))
        consumer.acknowledge(msg)

        if len(batch) >= batch_size:
            print(f"aggregated batch: {batch}")
            batch = []  # clear the batch after processing
    except Exception:
        consumer.negative_acknowledge(msg)

consumer.close()
client.close()

