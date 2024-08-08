import asyncio

"""

Gather allows us to execute multiples instance of coroutines in one instance

The even loop with manage the execution of these tasks, scheduling them ans switching
between them as neccessary


"""

async def task():
	print("Task started")
	await asyncio.sleep(1)
	print("Task completed")


async def main():
	await asyncio.gather(task(),task(),task())


if __name__ == '__main__':
	asyncio.run(main())




# another gather implementation
async def task(name, delay):

	print(f"Task {name} starting with delay of {delay}")

	await asyncio.sleep(delay)

	print(f"Task {name} finished")


	return f"Task {name} result"


async def main():

	tasks = [
		task("A",1),
		task("B",2),
		task("C",3)
	]


	results = await asyncio.gather(*tasks)

	for res in results:
		print(res)

if __name__ == '__main__':
	
	asyncio.run(main())