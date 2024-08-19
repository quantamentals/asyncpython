# Import necessary libraries
import asyncio  # for asynchronous programming
import datetime  # for getting the current date and time
import websockets  # for creating a WebSocket server

# Define an asynchronous function to handle WebSocket connections
async def time(websocket, path):
    try:
        # Run indefinitely
        while True:
            # Send the current date and time to the connected client
            await websocket.send(str(datetime.datetime.now()))
            # Wait for 1 second before sending the next update
            await asyncio.sleep(1)
    except websockets.exceptions.ConnectionClosedOK:
        # If the client disconnects, print a message
        print("Client disconnected")

# Define the main asynchronous function
async def main():
    # Print a message indicating the server is running
    print(f"Running server on localhost 5005")
    # Create a WebSocket server on localhost port 5005
    async with websockets.serve(time, 'localhost', 5005):
        # Run indefinitely to keep the server running
        await asyncio.Future()  # run forever

# Run the main function
asyncio.run(main())


"""

In this code, asyncio.Future() creates a future that never completes, so the await statement will wait forever, keeping the server running.

Let's break down the code:
asyncio.Future()

    This creates a new Future object, which is a special type of awaitable in asyncio.
    A Future represents a value that may not be available yet, but will be at some point in the future.
    When you create a Future object, it's initially in an "unresolved" state, meaning its value is not yet available.

await asyncio.Future()

    The await keyword is used to suspend the execution of the surrounding coroutine until the awaited object (in this case, the Future) is resolved.
    Since the Future created by asyncio.Future() is never resolved (i.e., its value is never set), the await statement will wait forever.
    This means that the execution of the surrounding coroutine (the main function) will be suspended indefinitely, keeping the server running.

In essence, asyncio.Future() creates a "dummy" future that never completes, and await asyncio.Future() waits for that future to complete, which never happens. This keeps the server running indefinitely, allowing it to continue accepting and handling WebSocket connections.



WebSockets offer a wide range of use cases. Here are some examples:

    Real-time updates: WebSockets enable bidirectional communication, allowing servers to push real-time updates to clients, such as live scores, stock prices, or news feeds.
    Live gaming: WebSockets facilitate real-time interactions between players, enabling features like multiplayer gaming, live chat, and collaborative gameplay.
    Chat applications: WebSockets power real-time chat and messaging apps, allowing for instant communication between users.
    Collaborative editing: WebSockets enable real-time collaboration on documents, spreadsheets, or code, allowing multiple users to edit simultaneously.
    Live streaming: WebSockets can be used for live video or audio streaming, enabling real-time communication between the broadcaster and viewers.
    IoT applications: WebSockets can be used to establish real-time communication between IoT devices and servers, enabling applications like remote monitoring and control.
    Financial applications: WebSockets can be used for real-time updates on financial data, such as stock prices or transaction notifications.
    Gaming notifications: WebSockets can be used to send real-time notifications to players, such as alerts for in-game events or updates.
    Social media updates: WebSockets can be used to push real-time updates to users, such as new posts, comments, or likes.
    Remote control: WebSockets can be used to establish real-time communication between devices, enabling remote control applications like remote desktop or robotic control.

These are just a few examples of the many use cases for WebSockets. The technology enables real-time communication and updates, making it a powerful tool for a wide range of applications.


Here's an example of how you can use WebSockets with asyncio, aioredis, and Uvicorn to handle trade stream data from Alpaca:
Step 1: Set up Uvicorn

    Install Uvicorn: pip install uvicorn
    Create a file main.py with the following code:

Python

import asyncio
from fastapi import FastAPI, WebSocket
from aioredis import create_redis

app = FastAPI()

redis = await create_redis("redis://localhost")

@app.websocket("/trade-stream")
async def trade_stream(websocket: WebSocket):
    await websocket.accept()
    async for message in websocket.iter_text():
        # Handle incoming message from client
        print(message)
        # Publish message to Redis channel
        await redis.publish("trade-stream", message)

    # Handle disconnection
    await websocket.close()

Step 2: Connect to Alpaca trade stream

    Install Alpaca SDK: pip install alpaca-trade-api
    Create a file alpaca_stream.py with the following code:

Python

import asyncio
from alpaca_trade_api.stream import Stream

async def alpaca_trade_stream():
    async with Stream() as stream:
        # Subscribe to trade stream
        await stream.subscribe_trades(alpaca_trade_handler)

        # Run indefinitely
        await asyncio.Future()

def alpaca_trade_handler(data):
    # Publish trade data to Redis channel
    redis.publish("trade-stream", data)

Step 3: Run Uvicorn and Alpaca stream

    Run Uvicorn: uvicorn main:app --host 0.0.0.0 --port 5000
    Run Alpaca stream: python alpaca_stream.py

Step 4: Handle trade stream data in Redis

    Create a file trade_handler.py with the following code:

Python

import asyncio
from aioredis import create_redis

redis = await create_redis("redis://localhost")

async def handle_trade_stream():
    # Subscribe to Redis channel
    channel = await redis.subscribe("trade-stream")

    # Handle incoming trade data
    async for message in channel.iter():
        print(message)

    # Handle disconnection
    await channel.unsubscribe()

asyncio.run(handle_trade_stream())

This example sets up a WebSocket endpoint with Uvicorn, connects to the Alpaca trade stream using the Alpaca SDK, publishes trade data to a Redis channel, and handles incoming trade data in a separate script using aioredis.
"""


