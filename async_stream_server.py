import asyncio
from alpaca_trade_api.stream import Stream
import os
from dotenv import load_dotenv
load_dotenv()

ALPACA_API_KEY = os.getenv('ALPACA_PAPER_API_KEY')
ALPACA_SECRET_KEY = os.getenv('ALPACA_PAPER_API_SECRET')

# async def handle_client(reader, writer):
#     try:
#         writer.write(b'HTTP/1.1 200 OK\r\n')
#         writer.write(b'Content-Type: text/event-stream\r\n\r\n')

#         stream = Stream(ALPACA_API_KEY, ALPACA_SECRET_KEY, raw_data=True)
#         stream.subscribe_crypto_quotes(
#             lambda q: writer.write(f"data: quote {q}\n\n".encode()),
#             'BTCUSD'
#         )
#         stream.subscribe_crypto_trades(
#             lambda t: writer.write(f"data: trade {t}\n\n".encode()),
#             'BTCUSD'
#         )

#         @stream.on_bar('BTCUSD')
#         async def _(bar):
#             writer.write(f"data: bar {bar}\n\n".encode())

#         await stream.run()
#     except Exception as e:
#         print(f"Error handling client request: {e}")
#     finally:
#         writer.close()
#         await writer.wait_closed()

# async def main():
#     server = await asyncio.start_server(handle_client, 'localhost', 8888)

#     async with server:
#         await server.serve_forever()

# if __name__ == '__main__':
#     asyncio.run(main())

# import asyncio
# import websockets
# import json
# import os

# import asyncio
# import aiohttp
# import json

# from dotenv import load_dotenv
# load_dotenv()

# ALPACA_API_KEY = os.getenv('ALPACA_PAPER_API_KEY')
# ALPACA_SECRET_KEY = os.getenv('ALPACA_PAPER_API_SECRET')

# async def listen_to_sse_events(event_type):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(f'https://stream.data.alpaca.markets/v2/{event_type}?since=2023-01-01T00:00:00Z') as response:
#             async for line in response.content:
#                 if line.startswith(b'data: '):
#                     data = json.loads(line.decode('utf-8')[6:])
#                     print(data)
#                     # Process the data here
#                     # For example, save it to a database
#                     await save_to_db(data)

# async def connect_to_stream():
#     async with websockets.connect('wss://stream.data.alpaca.markets/v2/test') as websocket:
#         # Authenticate
#         auth_message = json.dumps({
#             "action": "auth",
#             "key": ALPACA_API_KEY,
#             "secret": ALPACA_SECRET_KEY
#         })
#         await websocket.send(auth_message)

#         # Subscribe to trades
#         subscribe_message = json.dumps({
#             "action": "subscribe",
#             "trades": ["FAKEPACA"]
#         })
#         await websocket.send(subscribe_message)

#         # Receive messages
#         while True:
#             message = await websocket.recv()
#             print(message)

# async def main():
#     await connect_to_stream()

# asyncio.run(main())


#VIP
# import asyncio
# import aiohttp
# import json
# import websockets
# import os

# from dotenv import load_dotenv
# load_dotenv()

# ALPACA_API_KEY = os.getenv('ALPACA_PAPER_API_KEY')
# ALPACA_SECRET_KEY = os.getenv('ALPACA_PAPER_API_SECRET')

# async def listen_to_sse_events(event_type):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(f'https://stream.data.alpaca.markets/v2/{event_type}?since=2023-01-01T00:00:00Z') as response:
#             async for line in response.content:
#                 if line.startswith(b'data: '):
#                     data = json.loads(line.decode('utf-8')[6:])
#                     print(data)
#                     await save_to_file(data)

# async def connect_to_stream():
#     try:
#         async with websockets.connect('wss://stream.data.alpaca.markets/v2/test') as websocket:
#             # Authenticate
#             auth_message = json.dumps({
#                 "action": "auth",
#                 "key": ALPACA_API_KEY,
#                 "secret": ALPACA_SECRET_KEY
#             })
#             await websocket.send(auth_message)

#             # Subscribe to trades
#             subscribe_message = json.dumps({
#                 "action": "subscribe",
#                 "trades": ["FAKEPACA"]
#             })
#             await websocket.send(subscribe_message)

#             # Receive messages
#             while True:
#                 message = await websocket.recv()
#                 print(message)
#                 await save_to_file(message)
#     except websockets.exceptions.InvalidStatusCode as e:
#         print(f"Invalid status code: {e.status_code}")
#     except websockets.exceptions.ConnectionClosed as e:
#         print(f"Connection closed: {e.code} {e.reason}")
#     except Exception as e:
#         print(f"Error: {e}")


# async def save_to_file(data):
#     with open('data.txt', 'a') as file:
#         file.write(json.dumps(data) + '\n')

# async def main():
#     tasks = [listen_to_sse_events('account'), connect_to_stream()]
#     await asyncio.gather(*tasks)

# asyncio.run(main())

import asyncio
import websockets
import json
import os

from dotenv import load_dotenv
load_dotenv()

ALPACA_API_KEY = os.getenv('ALPACA_PAPER_API_KEY')
ALPACA_SECRET_KEY = os.getenv('ALPACA_PAPER_API_SECRET')

async def listen_to_sse_events(event_type):
    url = f"wss://stream.data.alpaca.markets/v2/{event_type}?since=2023-01-01T00:00:00Z"
    print(f"Connecting to {url}")
    try:
        async with websockets.connect(url) as websocket:
            while True:
                message = await websocket.recv()
                if message.startswith("data: "):
                    data = json.loads(message[6:])
                    print(data)
                    await handle_event(data)
                elif message == ":heartbeat":
                    print("Heartbeat received")
                else:
                    print(f"Unknown message: {message}")
    except websockets.exceptions.InvalidStatusCode as e:
        print(f"Invalid status code: {e.status_code}")
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed: {e.code} {e.reason}")
    except Exception as e:
        print(f"Error: {e}")

async def handle_event(data):
    # Handle the event data here
    # For example, you can save it to a database or process it in some way
    print(f"Handling event: {data}")
    await save_to_file(data)

async def connect_to_stream():
    try:
        async with websockets.connect('wss://stream.data.alpaca.markets/v2/test') as websocket:
            # Authenticate
            auth_message = json.dumps({
                "action": "auth",
                "key": ALPACA_API_KEY,
                "secret": ALPACA_SECRET_KEY
            })
            await websocket.send(auth_message)

            # Subscribe to trades
            subscribe_message = json.dumps({
                "action": "subscribe",
                "trades": ["FAKEPACA"]
            })
            await websocket.send(subscribe_message)

            # Receive messages
            while True:
                message = await websocket.recv()
                print(message)
                await save_to_file(message)
    except websockets.exceptions.InvalidStatusCode as e:
        print(f"Invalid status code: {e.status_code}")
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed: {e.code} {e.reason}")
    except Exception as e:
        print(f"Error: {e}")

async def save_to_file(data):
    with open('data.txt', 'a') as file:
        file.write(json.dumps(data) + '\n')

async def main():
    tasks = [listen_to_sse_events('account'), connect_to_stream()]
    await asyncio.gather(*tasks)

asyncio.run(main())