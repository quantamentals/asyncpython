import asyncio

"""
Await is neccessary for collecting task results and releasing resources

We must await task when presenting its results or unveiling

each task come with a done() method to boolean check if completed

also comes with a cancelled() to check if a task has been canceled


most async applications are related to network operations

Every task object has a cancel method, we can also set timeouts for tasks

canceled task raises a canceled error exception which would need to be handled
"""

def sync_function():
	print('From sync function')

async def one():
	return 1

async def greet(timeout):
	await asyncio.sleep(timeout)
	return 'Hello World'


async def main():
	res1 = asyncio.create_task(one())
	res2 = asyncio.create_task(greet())


	sync_function()

	print(await res2)

	print("This can run first")
    
	print(await res1)

	sync_function()

asyncio.run(main())