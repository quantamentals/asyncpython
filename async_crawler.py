import asyncio
import aiohttp

class AsyncSession:
	def __init__(self, url):
		self.url = url

	async def __aenter__(self):
		self.session = aiohttp.ClientSession()
		response = await self.session.get(self.url)
		return response

	async def __aexit__(self, exception_type, exception_value, traceback):
		await self.session.close()


class ServerError(Exception):
	def __init__(self, message):
		self._message = message


	def __str__(self):
		return self._message


async def server_returns_error():
	await asyncio.sleep(3)
	raise ServerError('Failed to get data')


async def check(url: str) -> str:
    try:
        async with AsyncSession(url) as response:
            if response.status == 200:
                html = await response.text()
                return f'{url}: {html[:15]}'
            else:
                return f'{url}: Failed with status {response.status}'
    except Exception as e:
        return f'{url}: Failed with error {str(e)}'


async def main():
	# # If discrete i can insert coros manually
	# results  = await asyncio.gather(
	# 	check('https://facebook.com'),
	# 	check('https://youtube.com'),
	# 	check('https://verizon.com')
	# )


	# I have to unpack lists and tuples into the gather
	coros = [
		check('https://facebook.com'),
		check('https://youtube.com'),
		check('https://verizon.com')
	]
	results = await asyncio.gather(*coros) # will execute and finish in order submitted

	for res in results:
		print(res)

	# I can also use list comprehensions
	coros = [check(url) for url in ['https://facebook.com', 'https://youtube.com', 'https://verizon.com']]
	results = await asyncio.gather(*coros, server_returns_error(), return_exceptions=True)

	for res in results:
		print(res)

	# How we can execute such they return in the order by which they finish not submitted
	coros = [
		check('https://facebook.com'),
		check('https://youtube.com'),
		check('https://verizon.com')
	]
	for coro in asyncio.as_completed(coros): # allows us to get coros as they finish their work
		result = await coro
		print(result)


	# a technique for creating a group of task
	group1 = asyncio.gather( # if we do not await gather it will return a futures object
		check('https://facebook.com'),
		check('https://youtube.com'),
	)

	group2 = asyncio.gather(

		check('https://youtube.com'),
		check('https://google.com')
	)

	print(type(group2))

	groups = asyncio.gather(group1, group2)

	results = await groups

	for res in results:
		print(res)



asyncio.run(main())