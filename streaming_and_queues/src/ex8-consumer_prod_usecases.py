import pulsar

# 1. Database replication / CDC
def replicate_changes_to_data_lake(change_data):
    pass


# 2. Event driven architecture: services react to events in real-time
def process_event(event_data):
    pass


# 3. Real time analytics
def aggregate_data_for_analysis(stream_data):
    pass


# 4. Metrics collection for monitoring
def monitor_system_health(metrics_data):
    pass


# 5. Messaging in microservices: async communication
def process_order(order_data):
    pass


# 6. IoT: sensor processing
def process_sensor_data(sensor_data):
    pass


# 7. Log aggregation from various sources
def aggregate_logs(log_data):
    pass


# 8. Streaming for ML real time inference
def process_data_for_ml_inference(data):
    pass



client = pulsar.Client("pulsar://localhost:6650")
consumer = client.subscribe(
    "clases", 
    subscription_name="shared-subscription",
    initial_position=pulsar.InitialPosition.Earliest  # Start consuming from the earliest message
)

while True:
    msg = consumer.receive()
    try:
        data = msg.data().decode("utf-8")
        if "error" in data:
            print(f"alert: critical issue detected - {data}")
        consumer.acknowledge(msg)
    except Exception:
        consumer.negative_acknowledge(msg)







consumer.close()
client.close()










