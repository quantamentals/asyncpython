import asyncio

from faker import Faker

import redis

"""
Async comprehensions allow us to create lists, dictionaries or set
using asynchronous operation

Async comprehensions provide a concise way to create collections using
asynchronous operations

"""


async def my_coro(number):

	await asyncio.sleep(1)
	return number ** 2


async def main():

	numbers = [1,2,3,4,5]

	squared_numbers = [await my_coro(n) for n in numbers]

	print(squared_numbers)



# creating coroutines from async generators

faker = Faker('en_US')

async def get_user(n=1):
	for i in range(n):
		await asyncio.sleep(0.1)
		name, surname = faker.name_male().split()
		yield name, surname


async def main():
    from redis_om import get_redis_connection

    redis_conn = get_redis_connection()

    users_list = [name async for name in get_user(3)]
    print(users_list)

    user_dict = {name: surname async for name, surname in get_user(3)}
    print(user_dict)

    users_set = {name async for name in get_user(3)}
    print(users_set)

    [redis_conn.set(key, value) for key, value in user_dict.items()]


if __name__ == '__main__':
    asyncio.run(main())