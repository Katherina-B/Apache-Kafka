# Bitcoin Transaction Processing with Apache Kafka

## Requirements
 * [Docker 20+](https://www.docker.com/get-started)
 * [Python 3.11](https://www.python.org/downloads/release/python-3115/)

## Bootstraping your environment
```bash
$docker-compose up -d
$docker exec -it lb2-kafka-1 /usr/bin/kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic bitcoin_transaction
$pip install -r requirements.txt
```
## Run
```bash
# run in different terminal windows
python producer.py
python consumer.py
```
