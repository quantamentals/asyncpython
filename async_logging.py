import asyncio
import logging

class AsyncLogger:
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.queue = asyncio.Queue()

    async def log(self, level, message):
        await self.queue.put((level, message))

    async def process_logs(self):
        while True:
            level, message = await self.queue.get()
            self.logger.log(level, message)
            self.queue.task_done()

    async def start(self):
        asyncio.create_task(self.process_logs())

# Usage example
async def main():
    logger = AsyncLogger('my_logger')
    await logger.start()

    # Log some messages
    await logger.log(logging.INFO, 'This is an info message')
    await logger.log(logging.ERROR, 'This is an error message')

    # Wait for logs to be processed
    await logger.queue.join()

asyncio.run(main())