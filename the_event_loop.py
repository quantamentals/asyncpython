import asyncio
from threading import Thread
import sys

"""
The event loop is responsible for
	- scheduling and executing coroutines
	- Handling I/O operations (eg network, file i/o)
	- Managing timeouts and delays
	- dispatching events to appropriate callbacks or handlers


We use sleep to mimic some network or file i/o operation

The event loop enables concurrency by allowing multiple async task to run
simultaneously without blocking the main thread.

This is a type of cooperative multitasking where tasks voluntarily yield control
back to the event loop when they encounter an awaitable operation

get event loop checks if a loop is running and 
will return the loop whose pid matched the current process pid, if any


Since loops in asyncio are tightly coupled with the concept of loop
policies, it not advisable to create the loop instances via the loop
constructor

If not, get the thread-global LoopPolicy instance
that’s stored in a global variable in the asyncio
module.

If it is not set, instantiate it with the
DefaultLoopPolicy using a lock.

The loop_policy.get_event_loop
method instantiates a loop only if you are on the
main thread and assigns it to a thread local variable.

If you are not on the main thread and no running
loop is instantiated by other means, it will raise a
RuntimeError

--

asyncio.get_running_loop works differently. It will always return the
currently running loop instance if there is one running. If there is none, it
will raise a RuntimeError.

--

Since loops in asyncio are tightly coupled with the concept of loop
policies, it not advisable to create the loop instances via the loop
constructor


# To create a new event loop instance, we will use the asyncio.new_event_loop

Another gotcha is that we will attach the newly created loop to the
event loop policy’s watcher to make sure that our event loop monitors the
termination of newly spawned subprocesses on UNIX systems

Using the threading. Thread and the side-effect-free (besides event loop
policy creation) asyncio.new_event_loop APIs, we can create thread
instances that have unique event loop instances.

"""

"""
# The simplest implementation of an event loop
from queue import Queue

class EventLoop(Queue):

	def start(self):
		while True:
			function = self.get()
			function()


# determining if and which event loop is running

# option 1
loop = asyncio.get_event_loop()

print(loop)

# option 2
try:
	loop = asyncio.get_running_loop()

except RuntimeError:
	print('No Loop Running')

"""

"""

######################################
# Creating an event loop from scratch
######################################

# creating a new event loop instance correctly
loop = asyncio.new_event_loop()
print('the first loop',loop) # Print the loop

# set the event loop, so the global asyncio.get_event_loop function can retrieve it
asyncio.set_event_loop(loop)

# attaching a watcher 
if sys.platform != "win32":
	watcher = asyncio.get_child_watcher()
	watcher.attach_loop(loop)


class LoopShowerThread(Thread):

	def run(self):
		try:

			loop = asyncio.get_event_loop()
			print(loop)

		except RuntimeError:
			print("No event loop is in the thread!")


loop = asyncio.get_event_loop() # calling this in the main thread will not attach to child

print('the loop is in the main though',loop)

thread = LoopShowerThread()
thread.start()
thread.join()

"""



######################################
# Attaching an event loop to a thread
######################################


def create_event_loop_thread(worker, *args, **kwargs):

	def _worker(*args, **kwargs):

		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)

		try:
			loop.run_until_complete(worker(*args,**kwargs))
		finally:
			loop.close()	

	return threading.Thread(target=_worker, args=args, kwargs=kwargs)




