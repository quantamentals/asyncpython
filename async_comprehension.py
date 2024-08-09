import asyncio

"""
Async comprehensions allow us to create lists, dictionaries or set
using asynchronous operation

"""


async def my_coro(number):

	await asyncio.sleep(1)
	return number ** 2




async def main():

	numbers = [1,2,3,4,5]

	squared_numbers = [await my_coro(n) for n in numbers]

	print(squared_numbers)



if __name__ == '__main__':
	asyncio.run(main())