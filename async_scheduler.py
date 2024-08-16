
import asyncio 
import time 
import heapq

# dev level code

class SimpleTaskScheduler:


	def __init__(self):
		self.tasks = []


	def add_task(self, coro, delay):
		exec_time = time.time() + delay
		heapq.heappush(self.tasks, (exec_time, coro))


	async def run(self):

		while self.tasks:
			exec_time, coro = heapq.heappop(self.tasks)
			now = time.time()

			if now < exec_time:
				await asyncio.sleep(exec_time-now)

			try:
				print(f"executing {coro.__name__} at {time.time()}")
				await coro()

			except Exception as e:

				print(f"Task {coro.__name__} raised {e}")


async def sample_task():
	print(f"Task executed at {time.time()}")


async def main():
	scheduler = SimpleTaskScheduler()
	scheduler.add_task(sample_task, 2)
	scheduler.add_task(sample_task, 1)


	await scheduler.run()

# prod level code

import asyncio
import time
import heapq
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SimpleTaskScheduler:
    """
    A simple task scheduler that executes tasks at specified delays.
    """

    def __init__(self):
        """
        Initializes an empty task list.
        """
        self.tasks = []

    def add_task(self, coro, delay):
        """
        Adds a task (a coroutine) to the scheduler with a specified delay.

        Args:
            coro (coroutine): The task to be executed.
            delay (float): The delay in seconds before executing the task.
        """
        try:
            exec_time = time.time() + delay
            heapq.heappush(self.tasks, (exec_time, coro))
            logger.info(f"Task {coro.__name__} added with delay {delay}")
        except Exception as e:
            logger.error(f"Error adding task {coro.__name__}: {e}")

    async def run(self):
        """
        Runs the scheduler. Executes tasks at their specified times.
        """
        while self.tasks:
            try:
                exec_time, coro = heapq.heappop(self.tasks)
                now = time.time()

                if now < exec_time:
                    await asyncio.sleep(exec_time - now)

                logger.info(f"Executing task {coro.__name__}")
                await coro()
                logger.info(f"Task {coro.__name__} executed successfully")
            except asyncio.CancelledError:
                logger.info("Task cancelled")
            except Exception as e:
                logger.error(f"Error executing task {coro.__name__}: {e}")


async def sample_task():
    """
    A simple coroutine that prints a message when executed.
    """
    try:
        print(f"Task executed at {time.time()}")
    except Exception as e:
        logger.error(f"Error in sample task: {e}")


async def main():
    """
    Creates a scheduler instance, adds tasks, and runs the scheduler.
    """
    try:
        scheduler = SimpleTaskScheduler()
        scheduler.add_task(sample_task, 2)
        scheduler.add_task(sample_task, 1)
        await scheduler.run()
    except Exception as e:
        logger.error(f"Error in main: {e}")


asyncio.run(main())

