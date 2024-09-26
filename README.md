# Kafka

There are many reasons for the adoption of Kafka :

     The publish - subscribe approach.
     Distributed architecture, for scalability (scaling).
     The connector system.
     Processing of data stream or Stream processing.

Another advantage of Kafka is its connector system Kafka Connect. Connectors are reusable components which, as the name suggests, allow different systems to be connected to Kafka.

Kafka connectors link:
https://docs.confluent.io/platform/current/connect/kafka_connectors.html

For this course, we will use Docker to start a Kafka cluster, the Zookeeper server needed to run it, and Kafka UI, an open source web interface to administer the cluster.
