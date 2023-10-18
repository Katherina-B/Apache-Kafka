# Bitcoin Transaction Processing with Apache Kafka

## Requirements
 * [Docker 20+](https://www.docker.com/get-started)
 * [Python 3.11](https://www.python.org/downloads/release/python-3115/)

## Bootstraping your environment
```bash
$docker-compose up -d
$docker exec lb2-kafka-1 create_topic.sh 
$pip install -r requirements.txt
```
## Run
```bash
# run in different terminal windows
python producer.py
python consumer.py
```
