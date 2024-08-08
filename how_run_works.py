import asyncio


"""
 The run method creates and starts an event loop


 We can check the amount of tasks running on the eventloop with all_task()


"""

async def coro(message):
	print(message)
	await asyncio.sleep(1)
	print(message)


async def main():
	print(asyncio.all_tasks())
	print('-- main beginning: just one task on the event loop')
	asyncio.create_task(coro('text'))
	print(asyncio.all_tasks())
	print('Now two tasks on the event loop')
	await asyncio.sleep(1)
	print('-- main done')


asyncio.run(main())