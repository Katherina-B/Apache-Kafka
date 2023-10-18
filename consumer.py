import asyncio
import websockets
import json

async def consumer():
    url = "wss://ws.bitstamp.net/"
    async with websockets.connect(url) as websocket:
        channel_data = {
            "event": "bts:subscribe",
            "data": {
                "channel": "live_orders_btcusd"
            }
        }
        await websocket.send(json.dumps(channel_data))
        top_10_transactions = []

        while True:
            message = await websocket.recv()
            data = json.loads(message)
            transaction = data.get('data')  # Use get to handle potential missing keys

            if transaction is not None:
                print(transaction)  # Print the received data

                # Update top 10 transactions
                top_10_transactions.append(transaction)
                top_10_transactions = sorted(top_10_transactions, key=lambda x: x.get('price', 0), reverse=True)[:10]

                # Print top 10 transactions
                print('\nTop 10 Transactions:')
                for idx, transaction in enumerate(top_10_transactions, start=1):
                    print(f'{idx}. Amount: {transaction.get("amount_str", "")}, Price: {transaction.get("price_str", "")}')

# Run the consumer
asyncio.get_event_loop().run_until_complete(consumer())
