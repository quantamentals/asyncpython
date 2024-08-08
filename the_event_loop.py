import asyncio
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

--

asyncio.get_running_loop works differently. It will always return the
currently running loop instance if there is one running. If there is none, it
will raise a RuntimeError.

--

Since loops in asyncio are tightly coupled with the concept of loop
policies, it not advisable to create the loop instances via the loop
constructor

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


# creating a new event loop instance correctly
loop = asyncio.new_event_loop()
print(loop) # Print the loop
asyncio.set_event_loop(loop)
if sys.platform != "win32":
	watcher = asyncio.get_child_watcher()
	watcher.attach_loop(loop)