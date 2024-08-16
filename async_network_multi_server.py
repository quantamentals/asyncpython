"""

In the context of asyncio and network programming, reader and writer are objects that represent the connection to a client.

    Reader: The reader object is used to receive data from the client. It's an asynchronous iterator that yields the data received from the client. You can think of it as a stream of incoming data from the client.
    Writer: The writer object is used to send data to the client. It provides methods to write data to the client, such as write() and drain(). You can think of it as a stream of outgoing data to the client.

Together, the reader and writer objects allow you to communicate with the client asynchronously, meaning you can handle multiple clients concurrently without blocking.
Here's a simple analogy to help illustrate the concept:

    Reader: Imagine a mailbox where you receive letters (data) from someone.
    Writer: Imagine a mailbox where you send letters (data) to someone.

In this analogy, the reader is like the mailbox where you receive letters, and the writer is like the mailbox where you send letters. Just as you can receive and send letters through the mailboxes, you can receive and send data through the reader and writer objects in asyncio.
In the context of the chat server code, the reader is used to receive messages from the client, and the writer is used to send messages back to the client.


"""
# Import the asyncio library, which provides support for asynchronous I/O
import asyncio

# Create a set to store the writers for all connected clients
clients = set()

# Define an asynchronous function to handle client requests
async def handle_client_requests(reader, writer):
    # Add the writer for the current client to the set of clients
    clients.add(writer)

    try:
        # Loop indefinitely to handle multiple messages from the client
        while True:
            # Read up to 1024 bytes of data from the client
            data = await reader.read(1024)

            # If no data is received, the client has disconnected
            if not data:
                break

            # Decode the received data into a string
            message = data.decode('utf-8', errors='replace')

            # Print the received message to the console
            print(f"Received from client: {message}")

            # Send an acknowledgement back to the client
            writer.write(b'Message received')
            await writer.drain()

            # Broadcast the message to all connected clients
            for client in list(clients):
                # Don't send the message back to the client that sent it
                if client != writer:
                    client.write(data)
                    await client.drain()

    finally:
        # Remove the writer for the current client from the set of clients
        clients.remove(writer)

        # Close the writer to free up resources
        writer.close()

        # Wait for the writer to be fully closed
        await writer.wait_closed()


# Define the main asynchronous function
async def main():
    # Start an asyncio server on localhost port 8888
    server = await asyncio.start_server(handle_client_requests, 'localhost', 8888)

    # Use an asynchronous context manager to ensure the server is properly cleaned up
    async with server:
        # Start the server and serve clients indefinitely
        await server.serve_forever()


# Check if this script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Run the main function using asyncio
    asyncio.run(main())