import asyncio
import aiohttp
from bs4 import BeautifulSoup

# basic web scrape
async def fetch(url):
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as response:
			return await response.text()


async def main():
	url = 'https://example.com'
	html = await fetch(url)
	print(html)


# concurrent web scraping
async def fetch(session, url):
	async with session.get(url) as response:
		return await response.text()


async def main():

	urls = [
		'https://example.com',
		'https://example.org',
		'https://example.net'
	]

	async with aiohttp.ClientSession() as session:
		tasks = []

		for url in urls:
			task = asyncio.create_task(fetch(session, url))
			tasks.append(task)

		html_contents = await asyncio.gather(*tasks)

		for html in html_contents:
			print(len(html))


# Parsing content asyncly
async def fetch(session, url):
	async with session.get(url) as response:
		return await response.text()

async def parse(html):
	soup = BeautifulSoup(html, 'html.parser')
	title = soup.title.text
	print(f'Title: {title}')


async def main():
	url = 'https://example.com'


	async with aiohttp.ClientSession() as session:

		html = await fetch(session, url)

		await parse(html)

if __name__ == '__main__':
	asyncio.run(main())