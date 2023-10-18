from confluent_kafka import Producer
import websocket
import json

# Initialize Kafka Producer
producer_conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(producer_conf)

# Define the WebSocket URL
websocket_url = "wss://ws.bitstamp.net"

def on_message(ws, message):
    try:
        data = json.loads(message)
        if 'data' in data and 'channel' in data and data['channel'] == 'live_orders_btcusd':
            bitcoin_transaction = data['data']
            producer.produce('bitcoin_transactions', json.dumps(bitcoin_transaction).encode('utf-8'))
            producer.poll(0)
            #print(f"Sent: {bitcoin_transaction}")
            print(f"Sent: bitcoin_transaction")
    except Exception as e:
        print(f"Error: {e}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws):
    print("Closed")

def on_open(ws):
    print("Opened")
    ws.send('{"event":"bts:subscribe","data":{"channel":"live_orders_btcusd"}}')

if __name__ == "__main__":
    ws = websocket.WebSocketApp(websocket_url, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
