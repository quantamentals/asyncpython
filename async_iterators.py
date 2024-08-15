"""

Objects that can be iterated return instances of the __iter__() and __next__() methods.

"""
from redis import asyncio as aioredis
import asyncio
from redis_om import get_redis_connection


class A:


	def __iter__(self):
		self.x = 0
		return self

	def __next__(self):

		if self.x > 2:
			raise StopIteration

		else:
			self.x += 1
			return self.x


class RedisReader:

	def __init__(self, redis, keys):

		self.redis=redis
		self.keys = keys


	def __aiter__(self):
		self.ikeys = iter(self.keys)
		return self


	async def __anext__(self):
		try:
			key = next(self.ikeys)

		except StopIteration:
			raise StopAsyncIteration



		async with self.redis.client() as connection:
			value = await connection.get(key)

		return value


async def main():
    redis = await aioredis.from_url('redis://localhost')

    # Get all keys from Redis
    keys = [key.decode() for key in await redis.keys('*')]
    print(keys)

    # Read values from Redis using RedisReader
    for key in keys:
        value = await redis.get(key)
        print(value)

    # Alternatively, use RedisReader with async for
    async for value in RedisReader(redis, keys):
        print(value)

    # You can also call other coroutines here

asyncio.run(main())