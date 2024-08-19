"""

There are three main types of awaitabl objects: coroutines, Tasks and Futures

Coroutine: an async def function

Task: Allows schedulings of coroutines concurrently


Future: A future is a the promise-like object from js.
		Its like a placholder for a value that will be materialized in the future



Futures are helpful when we want to run non-async functions concurrently 
with Asyncio

There are two ways of executing futures for blocking tasks:

	- ProcessPoolExecutor: runs each of your workers in its own seperate child process
	 					   use case: CPU bound tasks such as ML,DB queries etc


	- ThreadPoolExecutor: runs each of the workers in seperate threads within the main process
						  use case: I/O bound tasks lik file reads or network requests to servers

"""

import asyncio
from concurrent.futures import ThreadPoolExecutor
import time 


a_future = None 
b_future = None 


def wait_on_b():
	return 5 

def wait_on_a():
	return 6 

def main():

	# this is how we run non async code using threadpools
	executor = ThreadPoolExecutor(max_workers=2) # shared vars
	print("Started at {time.strftime('%X')}")
	a_future = executor.submit(wait_on_a)
	b_future = executor.submit(wait_on_b)
	print(a_future)
	print(b_future)

	time.sleep(2)

	print(a_future.result())
	print(b_future.result())

	print(f"finished at {time.strftime('%X')}")



from concurrent.futures import ProcessPoolExecutor
from time import sleep


def task(message):
	print("Sleeping...")
	sleep(2)
	print("Done Sleeping")
	return message

def main():
	executor = ProcessPoolExecutor(4) # no shared vars
	future = executor.submit(task, 'Completed')
	print(f"Future isDone Status {future.done()}")
	sleep(2)
	print(f'Future isDone Status {future.done()}')
	print(f'Future Result: {future.result()}')

if __name__ == '__main__':
	main()


