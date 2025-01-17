import asyncio
from threading import Thread
import threading
import sys
import os

"""
An event is a message that is emitted in a certain condition by one part of
the program. A loop, on the other hand, is a construct that finishes under a
certain condition and executes a certain program until it does so.

An event loop therefore is a loop that allows one to subscribe to the
event transmission and register handlers/callbacks. It enables the program
to run in an asynchronous fashion. 

The event loop delegates all the events
it receives to their respective callbacks.

The event loop is responsible for
	- Scheduling and executing coroutines
	- Handling I/O operations (eg network, file i/o)
	- Managing timeouts and delays
	- dispatching events to appropriate callbacks or handlers

A tick is the time unit of the event loop. It encompasses all the actions that happen in one
iteration step of the event loop.

Event loops in asyncio have four states they can be in:
	•Idle
	•Running
	•Stopped
	•Closed

They constitute the event loop lifecycle interface that all asyncio/third-­
party event loops need to provide for compatibility:
	•run_forever
	•run_until_complete

The run_forever method is called without a parameter, whereas the
run_until_complete method consumes a coroutine. 

To stop, we use the stop method and to close, we use the close method

The idle state is the state the loop is in after creation. It cannot consume any coroutine or any callback in this state.
In this state, loop.is_running returns the value False.

The running state is the state the loop is in after either calling loop.run_
forever or loop.run_until_complete.

In this state, the loop.is_running method returns the value True.


The loop enters the closed state by calling the close method. It can only
be called if the loop is not in the running state



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


AbstractEventLoop and BaseEventLoop represent 
two potential classes for an event loop implementation.


The AbstractEventLoop class defines the interface of an event loop in the
asyncio ecosystem. The interface methods can be roughly split into the
following sections:
	•Lifecycle methods (running, stopping, querying the
	state of, and closing the loop)
	•Scheduling methods
	•Callbacks
	•Coroutines
	•Future creation
	•Thread-related methods
	•I/O-related methods
	•Low-level APIs (socket, pipe, and reader/writer APIs)
	•High-level APIs (server, pipe, and subprocess-related
	methods)
	•Signal methods
	•Debug flag management methods

	 
The API is stable and can be subclassed in the case of a manual event
loop implementation

Despite being more high-level component based, the BaseEventLoop class
should not be used to create a manual loop implementation because its
API is not stable


Event loops are OS specific. This may affect API availability and the
speed of the event loop.
--

asyncio.get_running_loop works differently. It will always return the
currently running loop instance if there is one running. If there is none, it
will raise a RuntimeError.

--

Since loops in asyncio are tightly coupled with the concept of loop
policies, it not advisable to create the loop instances via the loop
constructor




Loops live in the context of a loop policy. The DefaultLoopPolicy scopes
the loop per thread and does not allow creation of a loop outside a main
thread via asyncio.get_event_loop. Hence, we must create a thread local
event loop via asyncio.set_event_loop(asyncio.new_event_loop()).
We then await the asyncio.run_until_complete completion inside
our internal worker function called _worker by waiting for the thread to be
joined via join_threads

	

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



async def print_coro(*args, **kwargs):
	print(f'Inside the print coro on {threading.get_ident()}:',(args, kwargs))

def start_threads(*threads):
	[t.start() for t in threads if isinstance(t, threading.Thread)]

def join_threads(*threads):
	[t.join() for t in threads if isinstance(t, threading.Thread)]


def main():
	workers = [create_event_loop_thread(print_coro) for i in range(10)]
	start_threads(*workers)
	join_threads(*workers)


if __name__ == '__main__':
	main()


# process local event loops in a primary-secondary setup
# with event loops running in all processes


pid_loops = {}


def get_event_loops():
	return pid_loops[os.getpid()]

def asyncio_init():

	pid = os.getpid()

	if pid not in pid_loops:

		pid_loops[pid] = asyncio.new_event_loop()
		pid_loops[pid].pid = pid


if __name__ == '__main__':

	# The shown solution provides a way to have one event loop per process on
 	# a unix system and cache it inside the pid_loops dict

	os.register_at_fork(after_in_parent=asyncio_init, after_in_child=asyncio_initn)

	if os.fork() == 0:
		# Child
		loop = get_event_loop()
		pid = os.getpid()
		assert pid == loop.pid
		print(pid)
	else:
		# Parent
		loop = get_event_loop()
		pid = os.getpid()
		assert pid == loop.pid
		print(pid)



"""



# The most basic control of the event loop
import asyncio 


async def my_corountine():
	print("Coroutine started")

	await asyncio.sleep(1)

	print("Coroutine completed")


if __name__ == "__main__":

	loop = asyncio.new_event_loop()
	try:

		loop.run_until_complete(my_corountine())
	
	finally:
		loop.close()