from uvicorn import run

async def app(scope, receive, send):
    if scope["type"] == "http":
        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": [(b"content-type", b"text/plain")]
        })
        await send({
            "type": "http.response.body",
            "body": b"Hello, World!"
        })

if __name__ == "__main__":
    run("uvicorn_intro:app", host="0.0.0.0", port=8000, log_level="info")


"""
Now that we've corrected the import statement, let's dive into the basics of Uvicorn using small examples:
1. Running an ASGI App
Uvicorn runs ASGI applications. Here's a simple example:
Python

from uvicorn import run

async def app(scope, receive, send):
    await send({"type": "http.response.start", "status": 200})
    await send({"type": "http.response.body", "body": b"Hello, World!"})

run("example:app", host="0.0.0.0", port=8000)

This code defines a simple ASGI app that returns "Hello, World!" and runs it with Uvicorn.
2. Handling HTTP Requests
Uvicorn handles HTTP requests by calling the ASGI app's __call__ method:
Python

from uvicorn import run

async def app(scope, receive, send):
    if scope["type"] == "http":
        await send({"type": "http.response.start", "status": 200})
        await send({"type": "http.response.body", "body": b"Hello, HTTP!"})

run("example:app", host="0.0.0.0", port=8000)

This code checks if the incoming request is an HTTP request and returns a custom response.
3. WebSockets
Uvicorn supports WebSockets out of the box:
Python

from uvicorn import run

async def app(scope, receive, send):
    if scope["type"] == "websocket":
        await send({"type": "websocket.accept"})
        while True:
            message = await receive()
            if message["type"] == "websocket.text":
                await send({"type": "websocket.text", "text": "Echo: " + message["text"]})

run("example:app", host="0.0.0.0", port=8000)

This code establishes a WebSocket connection and echoes incoming messages.
4. Command-Line Interface
Uvicorn provides a command-line interface to run ASGI apps:
Bash

uvicorn example:app --host 0.0.0.0 --port 8000

This command runs the ASGI app defined in the example module.
These examples demonstrate the basics of Uvicorn, including running ASGI apps, handling HTTP requests, supporting WebSockets, and using the command-line interface.


########################### Applications ##########################
import asyncio
from uvicorn import run

async def trading_event_loop():
    # Your trading event loop logic here
    while True:
        # Handle trading events
        await asyncio.sleep(1)

async def app(scope, receive, send):
    # Your ASGI app logic here
    await send({"type": "http.response.start", "status": 200})
    await send({"type": "http.response.body", "body": b"Hello, World!"})

async def main():
    # Create a background task for the trading event loop
    trading_task = asyncio.create_task(trading_event_loop())
    # Run the ASGI app
    await run("example:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    asyncio.run(main())



###

Here's an updated example that allows specific POST requests to submit events to the trading event loop asynchronously:
Python

import asyncio
from uvicorn import run

# Trading event loop
async def trading_event_loop():
    # Your trading event loop logic here
    while True:
        # Handle trading events
        await asyncio.sleep(1)

# Event queue to submit events to the trading event loop
event_queue = asyncio.Queue()

# ASGI app
async def app(scope, receive, send):
    if scope["type"] == "http":
        if scope["method"] == "POST":
            # Handle POST request
            body = await receive()
            event = await asyncio.get_event_loop().run_in_executor(None, lambda: body.json())
            # Submit event to the trading event loop
            await event_queue.put(event)
            await send({"type": "http.response.start", "status": 201})
            await send({"type": "http.response.body", "body": b"Event submitted"})
        else:
            await send({"type": "http.response.start", "status": 405})
            await send({"type": "http.response.body", "body": b"Method not allowed"})

# Background task to consume events from the queue
async def consume_events():
    while True:
        event = await event_queue.get()
        # Handle event in the trading event loop
        await trading_event_loop_handle_event(event)

async def trading_event_loop_handle_event(event):
    # Your event handling logic here
    print(f"Received event: {event}")

async def main():
    # Create a background task for the trading event loop
    trading_task = asyncio.create_task(trading_event_loop())
    # Create a background task to consume events from the queue
    consume_task = asyncio.create_task(consume_events())
    # Run the ASGI app
    await run("example:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    asyncio.run(main())

In this updated example:

    We create an event_queue to submit events to the trading event loop.
    We update the ASGI app to handle POST requests and submit events to the event_queue.
    We create a background task consume_events to consume events from the event_queue and handle them in the trading event loop.

Now, when a POST request is made to the ASGI app, it will submit the event to the event_queue, which will be consumed by the consume_events task and handled in the trading event loop.Here's an updated example that allows specific POST requests to submit events to the trading event loop asynchronously:
Python

import asyncio
from uvicorn import run

# Trading event loop
async def trading_event_loop():
    # Your trading event loop logic here
    while True:
        # Handle trading events
        await asyncio.sleep(1)

# Event queue to submit events to the trading event loop
event_queue = asyncio.Queue()

# ASGI app
async def app(scope, receive, send):
    if scope["type"] == "http":
        if scope["method"] == "POST":
            # Handle POST request
            body = await receive()
            event = await asyncio.get_event_loop().run_in_executor(None, lambda: body.json())
            # Submit event to the trading event loop
            await event_queue.put(event)
            await send({"type": "http.response.start", "status": 201})
            await send({"type": "http.response.body", "body": b"Event submitted"})
        else:
            await send({"type": "http.response.start", "status": 405})
            await send({"type": "http.response.body", "body": b"Method not allowed"})

# Background task to consume events from the queue
async def consume_events():
    while True:
        event = await event_queue.get()
        # Handle event in the trading event loop
        await trading_event_loop_handle_event(event)

async def trading_event_loop_handle_event(event):
    # Your event handling logic here
    print(f"Received event: {event}")

async def main():
    # Create a background task for the trading event loop
    trading_task = asyncio.create_task(trading_event_loop())
    # Create a background task to consume events from the queue
    consume_task = asyncio.create_task(consume_events())
    # Run the ASGI app
    await run("example:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    asyncio.run(main())

In this updated example:

    We create an event_queue to submit events to the trading event loop.
    We update the ASGI app to handle POST requests and submit events to the event_queue.
    We create a background task consume_events to consume events from the event_queue and handle them in the trading event loop.

Now, when a POST request is made to the ASGI app, it will submit the event to the event_queue, which will be consumed by the consume_events task and handled in the trading event loop.

Here's an updated example that uses the main function to fire a collection of background routines that monitor for orders, SSE events, and WebSocket streams all at startup:
Python

import asyncio
from uvicorn import run

# Background routines
async def monitor_orders():
    # Your order monitoring logic here
    while True:
        # Check for new orders
        await asyncio.sleep(1)

async def monitor_sse_events():
    # Your SSE event monitoring logic here
    while True:
        # Check for new SSE events
        await asyncio.sleep(1)

async def monitor_websocket_streams():
    # Your WebSocket stream monitoring logic here
    while True:
        # Check for new WebSocket messages
        await asyncio.sleep(1)

# ASGI app
async def app(scope, receive, send):
    # Your ASGI app logic here
    await send({"type": "http.response.start", "status": 200})
    await send({"type": "http.response.body", "body": b"Hello, World!"})

async def main():
    # Create background tasks for each routine
    order_task = asyncio.create_task(monitor_orders())
    sse_task = asyncio.create_task(monitor_sse_events())
    ws_task = asyncio.create_task(monitor_websocket_streams())
    # Run the ASGI app
    await run("example:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    asyncio.run(main())

In this example:

    We define three background routines: monitor_orders, monitor_sse_events, and monitor_websocket_streams.
    We create background tasks for each routine using asyncio.create_task.
    We run the ASGI app using run.

When the main function is executed, it will start all three background routines concurrently, allowing them to monitor for orders, SSE events, and WebSocket streams simultaneously.
Note that you can adjust the logic inside each background routine to suit your specific needs.


Here are some pros and cons of the architecture:
Pros:

    Scalability: The architecture is designed to handle multiple background tasks concurrently, making it scalable for large-scale applications.
    Flexibility: The use of asyncio and background tasks allows for easy integration of different components and services.
    Real-time processing: The architecture enables real-time processing of events and data, making it suitable for applications that require timely responses.
    Decoupling: The ASGI app and background tasks are decoupled, allowing for independent development and deployment.

Cons:

    Complexity: The architecture introduces additional complexity due to the use of asyncio and background tasks.
    Error handling: Error handling becomes more complex due to the concurrent nature of the background tasks.
    Resource usage: The architecture may consume more resources (e.g., memory, CPU) due to the concurrent execution of background tasks.
    Debugging: Debugging becomes more challenging due to the asynchronous nature of the architecture.
    Dependence on asyncio: The architecture relies heavily on asyncio, which may not be suitable for all applications or environments.
    Limited support for blocking calls: The architecture is designed for non-blocking calls, which may limit its compatibility with libraries or services that rely on blocking calls.

Overall, the architecture is suitable for applications that require real-time processing, scalability, and flexibility. However, it may introduce additional complexity and require careful error handling and resource management.


To add async pub/sub with Redis and structuring, validation, and serialization of messages with Pydantic, you can follow these steps:
Step 1: Install required libraries
Install the required libraries using pip:

pip install aioredis pydantic

Step 2: Define Pydantic models for messages
Define Pydantic models for your messages to ensure structuring, validation, and serialization:
Python

from pydantic import BaseModel

class OrderMessage(BaseModel):
    order_id: int
    symbol: str
    quantity: int

class SSEMessage(BaseModel):
    event: str
    data: dict

Step 3: Create an async Redis client
Create an async Redis client using aioredis:
Python

import aioredis

redis_client = aioredis.from_url("redis://localhost")

Step 4: Define pub/sub functions
Define pub/sub functions to publish and subscribe to messages:
Python

async def publish_message(channel: str, message: BaseModel):
    await redis_client.publish(channel, message.json())

async def subscribe_to_channel(channel: str):
    async with redis_client.pubsub() as pubsub:
        await pubsub.subscribe(channel)
        while True:
            message = await pubsub.get_message()
            if message:
                yield message

Step 5: Integrate with the architecture
Integrate the pub/sub functions with the architecture:
Python

async def monitor_orders():
    async for message in subscribe_to_channel("orders"):
        order_message = OrderMessage.parse_raw(message["data"])
        # Process the order message

async def monitor_sse_events():
    async for message in subscribe_to_channel("sse"):
        sse_message = SSEMessage.parse_raw(message["data"])
        # Process the SSE message

Step 6: Publish messages
Publish messages to the Redis channels:
Python

async def publish_order_message(order_message: OrderMessage):
    await publish_message("orders", order_message)

async def publish_sse_message(sse_message: SSEMessage):
    await publish_message("sse", sse_message)

By following these steps, you can add async pub/sub with Redis and structuring, validation, and serialization of messages with Pydantic to your architecture.

Here's the complete code that combines the architecture with async pub/sub using Redis and Pydantic for message structuring, validation, and serialization:
Python

import asyncio
import aioredis
from pydantic import BaseModel
from uvicorn import run

# Define Pydantic models for messages
class OrderMessage(BaseModel):
    order_id: int
    symbol: str
    quantity: int

class SSEMessage(BaseModel):
    event: str
    data: dict

# Create an async Redis client
redis_client = aioredis.from_url("redis://localhost")

# Define pub/sub functions
async def publish_message(channel: str, message: BaseModel):
    await redis_client.publish(channel, message.json())

async def subscribe_to_channel(channel: str):
    async with redis_client.pubsub() as pubsub:
        await pubsub.subscribe(channel)
        while True:
            message = await pubsub.get_message()
            if message:
                yield message

# Background routines
async def monitor_orders():
    async for message in subscribe_to_channel("orders"):
        order_message = OrderMessage.parse_raw(message["data"])
        # Process the order message
        print(f"Received order message: {order_message}")

async def monitor_sse_events():
    async for message in subscribe_to_channel("sse"):
        sse_message = SSEMessage.parse_raw(message["data"])
        # Process the SSE message
        print(f"Received SSE message: {sse_message}")

async def monitor_websocket_streams():
    # Your WebSocket stream monitoring logic here
    while True:
        # Check for new WebSocket messages
        await asyncio.sleep(1)

# ASGI app
async def app(scope, receive, send):
    # Your ASGI app logic here
    await send({"type": "http.response.start", "status": 200})
    await send({"type": "http.response.body", "body": b"Hello, World!"})

# Publish messages
async def publish_order_message(order_message: OrderMessage):
    await publish_message("orders", order_message)

async def publish_sse_message(sse_message: SSEMessage):
    await publish_message("sse", sse_message)

async def main():
    # Create background tasks for each routine
    order_task = asyncio.create_task(monitor_orders())
    sse_task = asyncio.create_task(monitor_sse_events())
    ws_task = asyncio.create_task(monitor_websocket_streams())
    # Run the ASGI app
    await run("example:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    asyncio.run(main())

This code combines the architecture with async pub/sub using Redis and Pydantic for message structuring, validation, and serialization. It defines two Pydantic models for messages, creates an async Redis client, and defines pub/sub functions. The background routines use these pub/sub functions to monitor for messages, and the ASGI app runs concurrently with the background routines.


"""