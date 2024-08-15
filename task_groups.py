import asyncio

"""

Gather allows us to execute multiples instance of coroutines in one instance

The even loop with manage the execution of these tasks, scheduling them ans switching
between them as neccessary

the gather method has the ability to handle exceptions



The gather method is used to await multiple coroutines concurrently.

The event loop manages the execution of these coroutines, ensuring they run
concurrently.


in 
 
"""

async def task():
	print("Task started")
	await asyncio.sleep(1)
	print("Task completed")


async def main():
	await asyncio.gather(task(),task(),task())



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