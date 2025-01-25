import pulsar

# connect to the pulsar broker
client = pulsar.Client("pulsar://localhost:6650")

# create a consumer for the topic
consumer = client.subscribe("clases", subscription_name="shared-subscription")

# consume messages from the topic
while True:
    msg = consumer.receive()
    try:
        print(f"consumed: {msg.data().decode('utf-8')}")
        # acknowledge the message
        consumer.acknowledge(msg)
    except Exception:
        # negative acknowledgment in case of an error
        consumer.negative_acknowledge(msg)

# close the consumer and client (if needed)
consumer.close()
client.close()
