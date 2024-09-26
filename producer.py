from kafka import KafkaProducer


# kafka_producer = KafkaProducer(
#   bootstrap_servers="localhost:9092" # if there is only one broker 
#      # bootstrap_servers=["kafka1:9092", "kafka2:9093", "kafka3:9094"]
#      # bootstrap_servers=["localhost:9092", "localhost:9093", "localhost:9094"] # for outside of docker use
# )


kafka_producer = KafkaProducer(
  bootstrap_servers="localhost:9092"
)

for i in range(1, 30):
  kafka_producer.send(
    topic="the_test",
    value=f"New message # {i}".encode("utf-8"),
    # the key will be '0' for even messages, and '1' for odd messages
    key=f"{i % 2}".encode("utf-8")
  )

kafka_producer.flush()

