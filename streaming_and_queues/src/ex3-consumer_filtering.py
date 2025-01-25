import pulsar 

client = pulsar.Client("pulsar://localhost:6650")
consumer = client.subscribe("clases", subscription_name="shared-subscription")

while True:
    msg = consumer.receive()
    try:
        data = msg.data().decode("utf-8")
        if "filter" in data:
            print(f"processed: {data}")
        else:
            print(f"ignored: {data}")
        consumer.acknowledge(msg)
    except Exception:
        consumer.negative_acknowledge(msg)

consumer.close()
client.close()

