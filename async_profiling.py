"""

Profiling allow me to capture performance bottlenecks and employing logging to aid

in debugging



Here are some best practices and patterns for code profiling:
Best Practices:

    Identify Performance Bottlenecks: Focus on the most critical parts of the code that impact performance.
    Use Profiling Tools: Leverage profiling tools like CPU profilers, memory profilers, and tracing tools.
    Profile in Production: Profile in production environments to capture real-world usage patterns.
    Profile Regularly: Regularly profile code to detect performance regressions.
    Analyze and Optimize Hotspots: Focus on optimizing the most resource-intensive parts of the code.
    Use Profiling to Inform Design Decisions: Use profiling data to guide design choices and optimizations.

Patterns:

    Instrumentation: Add instrumentation to code to collect profiling data.
    Sampling: Use sampling techniques to collect profiling data at regular intervals.
    Tracing: Use tracing to collect detailed information about code execution.
    Call Graph Analysis: Analyze call graphs to understand function call relationships.
    Flame Graphs: Use flame graphs to visualize profiling data and identify hotspots.
    Profiling-Driven Refactoring: Refactor code based on profiling data to optimize performance.
    Continuous Profiling: Integrate profiling into continuous integration and deployment pipelines.
    Profiling in Stages: Profile code in different stages, such as development, testing, and production.

Some popular profiling tools include:

    gprof (GNU Profiler)
    Valgrind
    Intel VTune Amplifier
    Google Benchmark
    PyCharm Profiler (for Python)
    VisualVM (for Java)

By following these best practices and patterns, you can effectively use code profiling to identify performance bottlenecks, optimize code, and improve overall application performance.


When using time and asyncio in Python, here are some best patterns to follow:
Time

    Use time.perf_counter(): For measuring elapsed time, use time.perf_counter() instead of time.time() for higher resolution and accuracy.
    Avoid time.sleep(): In async code, avoid using time.sleep(); instead, use asyncio.sleep() to yield control to other tasks.
    Use time.time_ns(): For measuring time in nanoseconds, use time.time_ns() for higher precision.

Asyncio

    Use asyncio.create_task(): Create tasks using asyncio.create_task() instead of loop.create_task() for better readability.
    Use asyncio.gather(): Run multiple coroutines concurrently using asyncio.gather() for improved performance.
    Use asyncio.sleep(): Use asyncio.sleep() instead of time.sleep() to yield control to other tasks.
    Avoid blocking calls: In async code, avoid making blocking calls; instead, use async alternatives or run blocking code in a separate thread.
    Use asyncio.run(): Run the main entry point of your async application using asyncio.run() for better error handling.

Combining Time and Asyncio

    Measure async function execution time: Use time.perf_counter() to measure the execution time of async functions.
    Add timeouts to async operations: Use asyncio.wait_for() to add timeouts to async operations and avoid infinite waits.
    Schedule tasks with asyncio.sleep(): Schedule tasks to run at a later time using asyncio.sleep().

By following these patterns, you can effectively use time and asyncio to write efficient, concurrent, and well-structured async code in Python.


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

