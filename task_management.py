"""

Task management is the primary building blocs for asynchronous operations in AsyncIO

Understanding how to create, schedule and manage tasks is crucial to async app

An asyncio task is a wrapper around a coroutine that provides additional functionality
for managing its execution

By creating task we have ways to manage 

create task via asyncio.create_task

Tasks can be canceled()

Tasks have various states such as  PENDING, RUNNING, CANCELLED, and FINISHED

The _state attribute of a Task object provides its current state


The result of a completed Task can be obtained by waiting the Task object itself

"""
import asyncio

# simplest implementation
async def my_coroutine():
	print("Coroutine started")
	await asyncio.sleep(1) # represents some unit of work


async def main():
	task = asyncio.create_task(my_coroutine())
	await task


# canceling  a task
async def my_coroutine(delay):
	await asyncio.sleep(delay)
	print(f"Coroutine with delay {delay} completed")


async def main():

	task1 = asyncio.create_task(my_coroutine(1))
	task2 = asyncio.create_task(my_coroutine(2))

	await asyncio.sleep(1.5)
	task2.cancel()

	await asyncio.gather(task1, task2, return_exceptions=True)

# checking a task state
async def my_coroutine(delay):
	await asyncio.sleep(delay)
	return delay

async def main():

	task = asyncio.create_task(my_coroutine(2))
	print(f"Task status: {task._state}") # get task status


	result = await task
	print(f"Task Result: {result}")


# error handling in the task
async def my_coroutine():
	raise ValueError("Something went wrong")

async def main():
	task = asyncio.create_task(my_coroutine())
	try:
		await task
	except ValueError as e:
		print(f"Error occurred: {e}")


# to schedule and await multiple tasks

async def my_coroutine(delay):
	await asyncio.sleep(delay)
	print(f"Coroutine with delay {delay} completed")

async def main():

	tasks = [

		asyncio.create_task(my_coroutine(1)),
		asyncio.create_task(my_coroutine(2)),
		asyncio.create_task(my_coroutine(3)),
	]

	await asyncio.gather(*tasks)


if __name__ == "__main__":

	asyncio.run(main())