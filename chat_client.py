import asyncio


async def chat_client(name, host, port):

	reader, writer = await asyncio.open_connection(host, port)
	print(f"{name} connected to chart server {host}:{port}")


	async def send_messages():
		while True:
			message = input(f"{name}: ")
			writer.write(message.encode())
			await writer.drain()


	async def recieve_messages():
		while True:
			data = await reader.read(100)
			if not data:
				print("Disconnected from chat server")
				writer.close()
				break

			print(data.decode())


	send_task = asyncio.create_task(send_messages())
	recieve_task = asyncio.create_task(recieve_messages())
	await asyncio.gather(send_task, recieve_task)



if __name__ == '__main__':
	name = input("Enter your name: ")
	asyncio.run(chat_client(name,'localhost',5001))




"""
	# inner methods can be defined because they can be created
	# as task and then gathered
	# allows to create simple server or compound task with a simple interface

"""