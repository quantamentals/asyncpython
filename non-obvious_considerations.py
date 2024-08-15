import asyncio


"""

Await keyword does not immediately hand over control to the event loop to 
switch coroutines

As soon as python encounters an await that doesnt return a result immediately

Control is handed over to the event loop and then to another coroutine in the queue

"""
async def nothing():
	# await asyncio.sleep(0)
	print('Busy')

async def busy_loop():
	for i in range(10):
		await nothing()


async def normal():
	for i in range(10):

		# await asyncio.sleep(0)
		print('Normal coroutine')


async def main():
	
	await asyncio.gather(
		busy_loop(),
		normal()
	)


asyncio.run(main())