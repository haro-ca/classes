import pulsar

client = pulsar.Client("pulsar://localhost:6650")
consumer = client.subscribe("clases", subscription_name="shared-subscription")
producer = client.create_producer("clases-transformed")

while True:
    msg = consumer.receive()
    try:
        data = msg.data().decode("utf-8").upper()
        print(f"transformed: {data}")
        producer.send(data.encode("utf-8"))
        consumer.acknowledge(msg)
    except Exception:
        consumer.negative_acknowledge(msg)

consumer.close()
producer.close()
client.close()

