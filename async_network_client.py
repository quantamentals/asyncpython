import asyncio 


async def connect_to_server():

	reader, writer = await asyncio.open_connection('localhost', 8888)

	message = 'Hello Server'

	writer.write(message.encode())

	await writer.drain()


	data = await reader.read(1024)
	print(f'Recieved from server: {data.decode()}')


	writer.close()


	await writer.wait_closed()


if __name__ == '__main__':
	asyncio.run(connect_to_server())