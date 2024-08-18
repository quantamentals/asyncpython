"""

Profiling allow me to capture performance bottlenecks and employing logging to aid

in debugging


"""

import asyncio
import time
import logging


logging.basicConfig(level=logging.DEBUG, format="'%(asctime)s %(levelname)s:%(message)s'")

async def simulate_io_task(name, duration):
	logging.info(f"Task {name}: Starting with duration of {duration}")

	await asyncio.sleep(duration)

	logging.info(f"Task {name}: Completed")

	return duration



async def main():
	start_time = time.perf_counter()
	tasks = [simulate_io_task(f"Task{i}", i) for i in range(1, 4)]

	durations = await asyncio.gather(*tasks)
	total_duration = sum(durations)
	end_time = time.perf_counter()

	logging.info(f'All tasks completed in {end_time - start_time } seconds, total sleep duration was {total_duration} seconds')



asyncio.run(main())

