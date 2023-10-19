#!/bin/bash

# Викликаємо команду для створення топіка Kafka
/usr/bin/kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic bitcoin_transaction
