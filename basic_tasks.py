import asyncio

"""
Await is neccessary for collecting task results and releasing resources

We must await task when presenting its results or unveiling

each task come with a done() method to boolean check if completed

also comes with a cancelled() to check if a task has been canceled


most async applications are related to network operations

Every task object has a cancel method, we can also set timeouts for tasks

canceled task raises a canceled error exception which would need to be handled


using other built in methods we handle long runnings task without canceling them


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


"""

async def greet(timeout):
	await asyncio.sleep(timeout)
	return 'Hello World'


async def main():
	long_task = asyncio.create_task(greet(5))

	# # implement a timeout function
	# seconds = 0

	# while not long_task.done():
	# 	await asyncio.sleep(1)
	# 	seconds += 1

	# 	if seconds == 5:
	# 		long_task.cancel()

	# 	print('Time passed: ', seconds)

	# try:

	# 	await long_task

	# except asyncio.CancelledError:
	# 	print('The long task has been cancelled')

	# canceling with built in timeout
	# try:

	# 	result = await asyncio.wait_for(long_task, timeout=5)
	# 	print(result)

	# except asyncio.exceptions.TimeoutError:
	# 	print('The long task has been cancelled')

	# notifiying without canceling with built in shield
	try:

		result = await asyncio.wait_for(
			asyncio.shield(long_task), 
			timeout=3
		)
		print(result)

	except asyncio.exceptions.TimeoutError:
		print('The long task took longer than 3 seconds')
		result = await long_task
		print(result)



asyncio.run(main())