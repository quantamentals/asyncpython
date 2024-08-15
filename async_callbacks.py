"""

In some cases we may want to run an async operation and recieve the result
in a callback function


the asyncio.ensure_future function schedules the coroutine for execution
and returns a future object


the add_done_callback method on the future object allows you to register
a callback function to be called when the coroutine completes


The below code is a basic example of using asyncio in Python to run a coroutine and handle its result with a callback function. Here's a breakdown of what your code does:

    Import asyncio: You import the asyncio library, which provides support for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, and implementing network clients and servers.
    Define a callback function: The callback function is defined to handle the result of the coroutine once it's completed. It takes a future object as an argument, retrieves the result of the future using future.result(), and prints the result.
    Define a coroutine: The my_coroutine function is defined as an asynchronous coroutine using the async def syntax. It uses await asyncio.sleep(1) to pause its execution for 1 second, simulating an asynchronous operation. After the sleep, it returns the number 42.
    Create an event loop: In the if __name__ == "__main__": block, you create a new event loop using asyncio.new_event_loop(). The event loop is the core of asyncio's event-driven programming model.
    Schedule the coroutine: You create a coroutine object by calling my_coroutine(), then wrap it in a Task object using asyncio.ensure_future(coroutine). This schedules the coroutine to run in the event loop.
    Add a callback to the future: You add the callback function as a done callback to the future using future.add_done_callback(callback). This ensures that callback is called once the coroutine completes.
    Run the event loop: You run the event loop until the future is complete using loop.run_until_complete(future). This starts the event loop and runs until the coroutine finishes.
    Close the event loop: Finally, you close the event loop in the finally block to ensure it's properly cleaned up, regardless of whether an exception occurred.

Your code demonstrates a basic pattern for running coroutines and handling their results with callbacks in asyncio.



Futures in asyncio represent a value that may not yet be available, but will be at some point in the future. Here are some additional things you can do with the idea of a Future:

    Awaiting multiple futures: You can use asyncio.gather() to await multiple futures simultaneously.
    Timeouts: You can use asyncio.wait_for() to await a future with a timeout.
    Cancellation: You can cancel a future using future.cancel().
    Exception handling: You can use try-except blocks to handle exceptions raised by a future.
    Chaining coroutines: You can use asyncio.create_task() to create a new task that depends on the result of another task.
    Future callbacks: You can add multiple callbacks to a future using future.add_done_callback().
    Waiting for multiple futures: You can use asyncio.wait() to wait for multiple futures to complete.
    Asynchronous iteration: You can use async for to asynchronously iterate over a sequence of futures.

Here's an example of using some of these concepts:
Python

import asyncio

async def my_coroutine():
    await asyncio.sleep(1)
    return 42

async def main():
    # Create a future
    future = asyncio.create_task(my_coroutine())

    # Add a callback
    def callback(future):
        print(f"Callback received result: {future.result()}")

    future.add_done_callback(callback)

    # Await the future with a timeout
    try:
        result = await asyncio.wait_for(future, timeout=2)
        print(f"Main received result: {result}")
    except asyncio.TimeoutError:
        print("Timeout occurred")

asyncio.run(main())

This code demonstrates creating a future, adding a callback, and awaiting the future with a timeout.


Implementing a Future from scratch involves creating a class that represents a value that may not yet be available. Here's a simplified example of what a Future class could look like:
Python

class Future:
    def __init__(self):
        self._result = None
        self._exception = None
        self._callbacks = []
        self._done = False

    def result(self):
        if not self._done:
            raise Exception("Future not yet done")
        if self._exception:
            raise self._exception
        return self._result

    def exception(self):
        if not self._done:
            raise Exception("Future not yet done")
        return self._exception

    def done(self):
        return self._done

    def add_done_callback(self, callback):
        if self._done:
            callback(self)
        else:
            self._callbacks.append(callback)

    def set_result(self, result):
        if self._done:
            raise Exception("Future already done")
        self._result = result
        self._done = True
        for callback in self._callbacks:
            callback(self)

    def set_exception(self, exception):
        if self._done:
            raise Exception("Future already done")
        self._exception = exception
        self._done = True
        for callback in self._callbacks:
            callback(self)

This Future class has the following methods:

    __init__: Initializes the Future with no result or exception.
    result: Returns the result of the Future, raising an exception if it's not yet done or if an exception occurred.
    exception: Returns the exception of the Future, raising an exception if it's not yet done.
    done: Returns whether the Future is done.
    add_done_callback: Adds a callback to be called when the Future is done.
    set_result: Sets the result of the Future, marking it as done and calling all callbacks.
    set_exception: Sets the exception of the Future, marking it as done and calling all callbacks.

You can use this Future class like this:
Python

def callback(future):
    print(f"Callback received result: {future.result()}")

future = Future()
future.add_done_callback(callback)

# Simulate setting the result
future.set_result(42)

Note that this is a simplified example and a real-world implementation would likely involve more features and edge cases. The asyncio library's Future class, for example, has many additional methods and features.


"""

import asyncio

def callback(future):
	print(f"Callback recieved result: {future.result()}")

async def my_corountine():
	await asyncio.sleep(1)
	return 42 


if __name__ == "__main__":

	loop = asyncio.new_event_loop()

	try: 

		coroutine = my_corountine()
		future = asyncio.ensure_future(coroutine)
		future.add_done_callback(callback)
		loop.run_until_complete(future)

	finally:
		loop.close()