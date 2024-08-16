"""

While AsyncIO is designed for writing asynchronous code.

Its need to integrate with existing synch libraries or code

AsyncIO provides mechanisms to bridge the gap between async and sync 
code, allowing for integration and interoperability


The run_in_executor method allows running synchronous code in seperate
code in a separate thread or process pool

The run_in_executor metho is used to offload the synchronous operation
to a seperate thread preventing the event loop from being blocked

Sometimes its useful to wrap synchronous functions with asynchronous
wrappers to make them compatible with AsyncIO


In these wrappers the coroutine wraps the synchronous_operation 
function using run_in_executor

The maincorotine can then call the async_wrappper as if it were an
async function

"""

import asyncio
import time
import requests

def synchronous_operation():
	time.sleep(2)
	return "Result from synchronous operation"

async def main():
	loop = asyncio.get_running_loop()
	result = await loop.run_in_executor(None, synchronous_operation)
	print(result)


async def fetch_url(url):

	loop = asyncio.get_running_loop()
	response = await loop.run_in_executor(None, requests.get, url)
	return response.text


async def main():
	url = "https://example.com"
	data = await fetch_url(url)
	print(data)


def sync_blocking_operations():
	time.sleep(2)
	return "Operation completed"

# the async wrapper function
async def run_sync_in_thread_pool():
	loop = asyncio.get_running_loop()
	result = await loop.run_in_executor(None, sync_blocking_operations)
	print(result)

async def main():
	await run_sync_in_thread_pool()


if __name__ == "__main__":
	asyncio.run(main())