"""
AsyncIO provides a powerful foundation for building efficient and scalable client-server applications

With async techniques we can handle multiple connection concurrently, improving performance

asyncio.start_server can be userd to create an async server

we can then write coroutines to handle communication with each client

Here the server is able to read data fromthe cline tnad prints the recieves message
and then returns a response

"""


	import asyncio

	async def handle_client_requests(reader, writer):
		data = await reader.read(1024)
		message = data.decode()
		print(f"recieved from client: {message}")


		response = "Hello from server"

		writer.write(response.encode())

		await writer.drain()

		writer.close()
		await writer.wait_closed()


	async def main():

		server = await asyncio.start_server(handle_client_requests, 'localhost', 8888)

		async with server:
			await server.serve_forever()


	if __name__ == '__main__':
		
		asyncio.run(main())	
