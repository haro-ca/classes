import pulsar

client = pulsar.Client("pulsar://localhost:6650")
consumer = client.subscribe("clases", subscription_name="shared-subscription")

while True:
    msg = consumer.receive()
    try:
        print(f"consumed: {msg.data().decode('utf-8')}")
        consumer.acknowledge(msg)
    except Exception:
        consumer.negative_acknowledge(msg)

consumer.close()
client.close()

