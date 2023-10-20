from confluent_kafka import Consumer, KafkaException
import json

def consumer():
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'my_consumer_group',
        'auto.offset.reset': 'earliest'
    }

    consumer = Consumer(conf)
    topics = ['bitcoin_transactions'] 
    try:
        consumer.subscribe(topics)

        top_10_transactions = []

        while True:
            msg = consumer.poll(timeout=1000)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    print(f"Got end of partition event for {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")
                    continue
                else:
                    print(f"Error: {msg.error()}")
                    break

            # Розпакувати та обробити повідомлення
            try:
                data = json.loads(msg.value().decode('utf-8'))
                transaction = data.get('data')
            except Exception as e:
                print(f"Error decoding message: {e}")
                continue

            if transaction is not None:
                #print(transaction)  # Вивести отримані дані

                # Оновити та вивести топ-10 транзакцій
                top_10_transactions.append(transaction)
                top_10_transactions = sorted(top_10_transactions, key=lambda x: x.get('price', 0), reverse=True)[:10]

                print('\nTop 10 Transactions:')
                for idx, transaction in enumerate(top_10_transactions, start=1):
                    print(f'{idx}. Amount: {transaction.get("amount_str", "")}, Price: {transaction.get("price_str", "")}')

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

# Запустити консюмер
consumer()
