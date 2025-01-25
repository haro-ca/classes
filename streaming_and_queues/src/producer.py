from time import sleep
import pulsar

# connect to the pulsar broker
client = pulsar.Client("pulsar://localhost:6650")

# create a producer for the topic
producer = client.create_producer("clases")

# send messages to the topic
for i in range(101):
    message = f"error hello pulsar {i}"
    producer.send(message.encode("utf-8"))
    print(f"produced: {message}")
    sleep(0.1)

# close the producer and client
producer.close()
client.close()
