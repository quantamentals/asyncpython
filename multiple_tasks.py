import asyncio 

async def download_file(file_name):

	print(f"starting download {file_name}")

	await asyncio.sleep(2)

	print(f"Finished downloading {file_name}")

	return f"{file_name} downloaded"


async def main():

	file_list = ["file.txt", "file2.txt", "file3.txt"]

	download_coroutines = [download_file(file) for file in file_list]

	completed, pending = await asyncio.wait(download_coroutines, return_when=asyncio.ALL_COMPLETED)


	for task in completed:
		print(task.result())



asyncio.run(main())