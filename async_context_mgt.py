import asyncio
import aiohttp

"""

Context managers are used to perform some required action after we have done something

exp. close file after writing to it


Context managers are possible because of magic methods __enter__() and __exit__()



To understand async with is that the methods called from __enter__ and __exit__ are coroutines.h 
The open and close methods are coroutines on the __enter__ and __exit__

The methods __aenter__ and __aexit__ are implemented for async context managers






# what is an asyncronous context manager



# non context manager way
try: 

	file = open('filename.txt', 'w')
	file.write('hello world!')

except IOError:
	print("Unable to create file on disk")

finally:
	file.close()


# A Generic Context Manager


class GenericContextManager:


	def __init__(self, obj):
		self.obj = obj


	def __enter__(self):
		# This method should return the context 
		return self.obj


	def __exit__(self, exception_type, exception_value, traceback):
		if self.obj:
			self.obj.close()


# A file context manager implentation


class WriteToFile:


	def __init__(self, filename):
		self.filename = filenamett


	def __enter__(self):
		self.file_obj = open(self.filename,'w')
		return self.file_obj


	def __exit__(self, exception_type, exception_value, traceback):
		if self.file_obj:
			self.file_obj.close()


def main():

	with WriteToFile('test.txt') as f:

		f.write('A context manager from scratch')


if __name__ == '__main__':
	main()

"""


# creating a async context manager called a session

class AsyncSession:

	def __init__(self, url):

		self.url = url


	async def __aenter__(self):
		self.session = aiohttp.ClientSession()
		response = await self.session.get(self.url)
		return response

	async def __aexit__(self, exception_type, exception_value, traceback):
		await self.session.close()


async def check(url):
	async with AsyncSession(url) as response:
		
		html = await response.text()

		print(f'{url}: {html[:20]}')



async def main():

	await asyncio.create_task(check('http://www.google.com'))
	await asyncio.create_task(check('http://www.youtube.com'))
	await asyncio.create_task(check('http://www.udemy.com'))


asyncio.run(main())