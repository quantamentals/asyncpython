import asyncio
import ssl

async def connect_to_server():
    ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ssl_context.check_hostname = True
    ssl_context.load_default_certs()

    reader, writer = await asyncio.open_connection(
        'localhost', 8888, ssl=ssl_context)

    try:
        data = await reader.read(1024)
        message = data.decode()
        print(f"Received from server: {message}")

        writer.write("Hello from client".encode())
        await writer.drain()

    except ConnectionResetError as e:
        print(f"Connection reset by peer: {e}")

    finally:
        writer.close()
        await writer.wait_closed()

if __name__ == '__main__':
    asyncio.run(connect_to_server())