import asyncio 
import logging

"""
In Python's logging module, there are six levels of severity, each with its own purpose. Here are the levels, in order of increasing severity, along with examples:

    DEBUG (level 10)
        Detailed information, typically used for debugging purposes.
        Example: logger.debug("User logged in with username: %s", username)
    INFO (level 20)
        Confirmation that things are working as expected.
        Example: logger.info("User logged in successfully")
    WARNING (level 30)
        Indication that something unexpected happened, but the program can continue running.
        Example: logger.warning("Low disk space: %s bytes remaining", disk_space)
    ERROR (level 40)
        Due to a more serious problem, the program may be unable to continue running.
        Example: logger.error("Failed to connect to database: %s", error_message)
    CRITICAL (level 50)
        A serious error, indicating that the program itself may be unable to continue running.
        Example: logger.critical("System crashed: %s", error_message)
    NOTSET (level 0)
        The lowest level, used to disable logging for a specific module or logger.

When deciding which level to use, consider the following:

    DEBUG: Use for detailed, low-level information, typically only useful during development or debugging.
    INFO: Use for general information, such as user actions or system events.
    WARNING: Use for unexpected events that don't prevent the program from running.
    ERROR: Use for errors that prevent a specific task or function from completing.
    CRITICAL: Use for severe errors that may cause the entire program to fail.

Remember to adjust the logging level according to your needs, and consider using a configuration file to customize logging settings for different environments (e.g., development, testing, production).

##

Here are some ways to use logging to track the flow of async programs, identify potential issues, and generate confirmations:

    Log async function entries and exits: Use logger.debug to log when an async function is entered and exited, including the function name and any relevant parameters.
    Log await points: Log when an async function awaits another coroutine or task, including the awaited task's name.
    Log task and coroutine IDs: Include task or coroutine IDs in logs to track the execution flow and identify which tasks or coroutines are involved in an issue.
    Use log levels: Utilize different log levels (e.g., DEBUG, INFO, WARNING, ERROR) to categorize log messages based on their severity and importance.
    Log exceptions: Catch and log exceptions in async functions to identify and diagnose errors.
    Log key events and milestones: Log important events, such as user interactions, database queries, or network requests, to track the program's flow.
    Generate confirmations: Use logging to generate confirmations, such as "User created successfully" or "Data saved to database."

Example:
Python

async def my_coroutine():
    logger.debug("Entering my_coroutine")
    try:
        await another_coroutine()
        logger.info("Another coroutine completed successfully")
    except Exception as e:
        logger.error("Error in another_coroutine: %s", e)
    finally:
        logger.debug("Exiting my_coroutine")

Some popular logging libraries for async Python programs include:

    Python's built-in logging module: Provides basic logging functionality.
    loguru: Offers advanced features like log formatting, filtering, and rotation.
    structlog: Allows for structured logging, making it easier to parse and analyze logs.

By following these best practices and using a suitable logging library, you can effectively track the flow of your async programs, identify potential issues, and generate confirmations.


Here are some design patterns for logging async applications:

    Contextual Logging: Include context information like user ID, request ID, or session ID in logs to track events across multiple components.
    Correlation IDs: Use a unique ID to correlate logs across different parts of the application, making it easier to trace a request or task.
    Structured Logging: Use a structured format like JSON or key-value pairs to log data, making it easier to parse and analyze.
    Logging Decorators: Create decorators to log function entries, exits, and exceptions, reducing boilerplate code.
    Async-Safe Logging: Ensure logging is thread-safe and async-safe to avoid logging-related deadlocks or crashes.
    Centralized Logging: Use a centralized logging service or framework to collect, process, and store logs from multiple components.
    Log Aggregation: Aggregate logs from multiple sources, making it easier to analyze and monitor application behavior.
    Real-time Logging: Implement real-time logging to monitor application behavior as it happens.
    Error Tracking: Use logging to track errors and exceptions, making it easier to diagnose and fix issues.
    Log Retention: Implement log retention policies to manage log storage and ensure compliance with regulations.

Some popular logging frameworks for async applications include:

    Sentry: Focuses on error tracking and monitoring.
    Loggly: Provides centralized logging and log aggregation.
    Splunk: Offers advanced log analysis and monitoring capabilities.
    ELK Stack (Elasticsearch, Logstash, Kibana): Provides a scalable logging solution with advanced analysis capabilities.

By applying these design patterns and using a suitable logging framework, you can create an effective logging strategy for your async application.



####

Debugging async programs often involves setting breakpoionts and inspecting variables


Pythons built-in breakpoint() function can be used to set breakpoints in AsyncIO code

When a breakpoint() function is hit the execution pauses and you can use the debbugger or python
REPL to inspect variables and step through code.

When the breakpoint is hit deugging tools are used to examine the state of the program


AsyncIO provides a debugging mode that can be enabled using, asyncio.get_event_loop().set_debug(True)

When debugt mode is enabled, AsyncIO will emit additional debug information and warnings


We enable debug mode before running a coroutine 

Any debugging information or warnings will be printed to the console, aiding in identifying and fixing issues


Remember logging allows us to track the flow of a program 


To maximize performance of my async applications the best practices include using logging,
profiling, debugging tools, avoiding blocking operations, and thorough testing

This is the path to building application reliability:


Here are some patterns that can help build reliability in async applications:

    Error Handling: Implement robust error handling mechanisms to catch and handle exceptions, ensuring the application can recover from failures.
    Retry Mechanisms: Use retry mechanisms, like exponential backoff, to handle transient failures and timeouts.
    Circuit Breakers: Implement circuit breakers to detect and prevent cascading failures by temporarily disabling failing components.
    Timeouts: Set timeouts for async operations to prevent indefinite waits and ensure the application remains responsive.
    Dead Letter Queues: Use dead letter queues to handle messages or tasks that cannot be processed, allowing for later analysis and recovery.
    Idempotence: Design idempotent operations to ensure that repeated executions have the same effect as a single execution.
    Transactionality: Use transactional mechanisms to ensure atomicity and consistency across multiple operations.
    Monitoring and Alerting: Implement monitoring and alerting to detect issues and notify teams for prompt action.
    Fallbacks: Provide fallbacks or defaults for failed operations to ensure the application remains functional.
    Testing and Validation: Thoroughly test and validate async code to ensure reliability and correctness.
    Async-Safe Data Structures: Use async-safe data structures to prevent data corruption and ensure thread safety.
    Leader Election: Implement leader election mechanisms to coordinate tasks and prevent duplicate work.
    Heartbeats: Use heartbeats to detect and recover from node or service failures.
    Load Balancing: Implement load balancing to distribute workloads and prevent overload failures.
    Chaos Engineering: Practice chaos engineering to simulate failures and test the application's reliability.

By applying these patterns, you can build more reliable async applications that can handle failures, recover from errors, and ensure consistent behavior.

"""

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

async def my_coroutine():
	logger.debug("Starting my_coroutine")
	await asyncio.sleep(1)
	logger.debug("Finished my coroutine")

async def main():
	logger.info("Starting main")
	await my_coroutine()
	logger.info("Finished main")

async def my_coroutine():
	await asyncio.sleep(1)
	breakpoint() # allows for using debugger
	await asyncio.sleep(1)

async def main():
	await my_coroutine()


async def my_coroutine():
	await asyncio.sleep(1)


async def main():
	asyncio.get_event_loop().set_debug(True)
	await my_coroutine()


if __name__ == "__main__":
	asyncio.run(main())