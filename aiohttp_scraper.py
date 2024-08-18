import logging
import asyncio
import aiohttp
from bs4 import BeautifulSoup

from aiohttp import ClientError

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

# error handling and retrying

logging.basicConfig(level=logging.INFO)

async def fetch_with_retry(session, url, max_retries=3):
    retries = 0
    delay = 1  # initial delay
    while retries < max_retries:

        try:

        	async with session.get(url) as response:
        		if response.status == 200:
        			print('running 200')
        			return await response.text()
        except aiohttp.ClientError as e:
            logging.error(f"Error fetching {url}: {e}")
            retries += 1
            await asyncio.sleep(delay)
            delay *= 2  # exponential backoff
    else:
        raise Exception(f"Failed to fetch {url} after {max_retries} retries")

async def main():
    url = "https://example.com/Invalid"

    async with aiohttp.ClientSession() as session:
        html = await fetch_with_retry(session, url)

        if html: 
            print("Successfully fetched the web page")
        else:
            print("Failed to fetch the webpage after multiple retries")

asyncio.run(main())
