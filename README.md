# Kafka Streaming Project

## Introduction

This project is a comprehensive setup of a **Kafka cluster** using **Docker Compose**. It includes **multiple Kafka brokers**, a **Zookeeper server**, and an open-source **Kafka UI** to manage and monitor the Kafka cluster. The project demonstrates core Kafka concepts such as message publishing, distributed architecture, scaling, and stream processing.

### Why Kafka?

Kafka is widely adopted due to its:

- **Publish-Subscribe Messaging Model**: Ideal for real-time data streaming and event-driven architectures.
- **Distributed Architecture**: Ensures scalability and fault tolerance.
- **Connector System**: Easily integrates with various systems through Kafka Connect.
- **Stream Processing**: Handles real-time data streams efficiently.

Kafka also offers **Kafka Connect**, a framework for connecting external systems to Kafka, enabling seamless data integration across different platforms. Read more about Kafka connectors [here](https://docs.confluent.io/platform/current/connect/kafka_connectors.html).

## Architecture Overview

The project sets up the following components:

1. **Zookeeper**: Responsible for managing the Kafka cluster and its brokers.
2. **Kafka Brokers**: Three brokers (broker-1, broker-2, and broker-3) to ensure high availability and fault tolerance.
3. **Kafka UI**: Provides a user-friendly interface to manage and monitor the Kafka cluster.
4. **Producers & Consumers**: Demonstrates producing and consuming messages from Kafka topics.

---

## Project Structure

The repository is organized as follows:

```
├── docker-compose.yml     # Docker Compose configuration for setting up Kafka cluster (3 brokers)
├── one-broker-docker-compose.yml # Docker compose with one broker
├── producer.py            # Python script to produce messages to a Kafka topic
├── consumer.py            # (Optional) Python script to consume messages from a Kafka topic
└── admin.py              #
└── README.md              # This file
```

### Key Services in Docker Compose

1. **Zookeeper**:

   - Manages the Kafka brokers.
   - Listens on port `2181`.

2. **Kafka Brokers**:

   - Three brokers to ensure fault tolerance and replication.
   - Broker 1: Listens on port `9091`.
   - Broker 2: Listens on port `9092`.
   - Broker 3: Listens on port `9093`.

3. **Kafka UI**:

   - Web interface to manage Kafka topics, producers, consumers, and configurations.
   - Accessible on port `8080`.

4. **Producers & Consumers**:
   - Produces and consumes messages for demonstration purposes.

---

## Getting Started

### Prerequisites

- **Docker** and **Docker Compose** installed on your system.
- Basic knowledge of Kafka, Docker, and Python.

### Setup Instructions

1. Clone this repository:

   ```bash
   git clone https://github.com/arifhaidari/kafka_streaming.git
   cd kafka-streaming-project
   ```

2. Start the Kafka cluster using Docker Compose:

   ```bash
   docker-compose up -d
   ```

   This will spin up the Zookeeper, Kafka brokers, and Kafka UI. Ensure that the services are up and running.

3. Verify that the Kafka UI is accessible by navigating to:

   ```
   http://localhost:8080
   ```

   You should be able to see all the Kafka brokers and manage topics, producers, and consumers.

---

## Usage

### Producing Messages

The `producer.py` script sends messages to a Kafka topic named `test`. It creates 30 messages for demonstration.

1. Run the Python producer script:

   ```bash
   python3 producer.py
   ```

2. This will send 30 messages to the `test` topic.

### Consuming Messages (Optional)

You can also use the Kafka UI to view messages in the `test` topic or implement a consumer script to read the messages.

---

### Explanation:

- **Kafka Brokers**: Three brokers are defined (kafka1, kafka2, kafka3), each with a unique `KAFKA_BROKER_ID`.
- **Zookeeper**: Manages the state of the Kafka brokers.
- **Kafka UI**: Connects to the three Kafka brokers for managing topics and messages.

---

## Best Practices

1. **Fault Tolerance**: Kafka's distributed architecture ensures that the system is highly available even if one or more brokers fail.
2. **Scalability**: Kafka scales horizontally by adding more brokers to handle larger amounts of data.
3. **High Throughput**: Kafka is designed to handle large streams of data in real-time with low latency.
4. **Replication Factor**: Set a proper replication factor to ensure that the data is replicated across brokers for reliability.

---

## Common Issues & Troubleshooting

- **Broker Connection Issues**: Ensure that the broker IDs and ports are correctly set up in the Docker Compose file and that they are not conflicting with other services on your machine.
- **Zookeeper Connection**: If Kafka brokers cannot connect to Zookeeper, check the `KAFKA_ZOOKEEPER_CONNECT` environment variable in the Docker Compose file.
- **Port Conflicts**: If you're running multiple brokers on the same machine, make sure to use distinct ports for each broker (as done in this project).

---

## Future Enhancements

- Add more brokers to increase fault tolerance and scalability.
- Introduce **Kafka Connect** for connecting to other data systems (e.g., databases, message queues).
- Implement **Kafka Streams** for real-time data processing and transformation.

---

## References

- **Kafka Documentation**: [Apache Kafka](https://kafka.apache.org/)
- **Kafka UI**: [Kafka UI GitHub](https://github.com/provectus/kafka-ui)
- **Docker Documentation**: [Docker](https://docs.docker.com/)

---

This project is open for contributions! Feel free to create issues or submit pull requests to improve the functionality.

## This project was developed under the supervision and instruction of the DataScientest Bootcamp.
