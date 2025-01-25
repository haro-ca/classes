import pulsar
from datetime import datetime

client = pulsar.Client("pulsar://localhost:6650")
consumer = client.subscribe("clases", subscription_name="shared-subscription")
producer = client.create_producer("clases-enriched")

while True:
    msg = consumer.receive()
    try:
        data = msg.data().decode("utf-8")
        enriched = f"{data} - enriched at {datetime.now()}"
        print(f"enriched: {enriched}")
        producer.send(enriched.encode("utf-8"))
        consumer.acknowledge(msg)
    except Exception:
        consumer.negative_acknowledge(msg)

consumer.close()
producer.close()
client.close()

