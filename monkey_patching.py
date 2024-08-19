import gevent
import requests
import timeit

from gevent import monkey

# monkey.patch_all()
monkey.patch_socket()

def make_request(pid):
	requests.get('http://google.com')
	print(f'Process {pid}')
	return ""


def synchronous():
	for i in range(1,10):
		make_request(i)


def asynchronous():
	threads = []
	for i in range(1,10):
		threads.append(gevent.spawn(make_request, i))
	gevent.joinall(threads)


print(f"Synchronous: {timeit.timeit(synchronous, number=1)}\n")
print(f"Asynchronous: {timeit.timeit(asynchronous, number=1)}")


"""
Your code compares the execution time of making multiple HTTP requests synchronously versus asynchronously using the gevent library.
Here's a breakdown of what your code does:

    The make_request function makes a GET request to Google and prints the process ID.
    The synchronous function makes 9 requests sequentially, waiting for each request to complete before making the next one.
    The asynchronous function creates 9 greenlets (lightweight threads) using gevent.spawn, each making a request. gevent.joinall is then used to wait for all greenlets to finish.
    The execution time of both functions is measured using timeit.timeit and printed to the console.

Note that gevent is a cooperative multitasking library, which means that greenlets yield control to other greenlets voluntarily, rather than being preempted by a scheduler like in traditional threading. This makes gevent more efficient for I/O-bound tasks like making HTTP requests.
Also, keep in mind that the timeit module runs the function multiple times to account for variability, but in this case, you're only running it once (number=1). If you want to get a more accurate average execution time, increase the number parameter.



The code you provided uses monkey patching indirectly through the gevent library.
Monkey patching is a way to extend or modify the runtime behavior of a module or class without changing its source code. In Python, this is often done by modifying the module's attributes at runtime.
In your code, gevent monkey patches the socket module to make it cooperative, allowing it to work with greenlets. This means that when you import gevent and use its API, it replaces the standard socket module's functions with its own implementations that are aware of greenlets.
Specifically, gevent replaces the following modules:

    socket
    ssl
    select
    time

By doing so, gevent enables cooperative multitasking for I/O-bound operations, like making HTTP requests, without requiring changes to the underlying library code (in this case, requests).
So while your code doesn't explicitly monkey patch anything, the gevent library does it under the hood to enable its asynchronous features.


The socket module is relevant because it's the foundation for network communication in Python. When you make an HTTP request using the requests library, it ultimately uses the socket module to establish a connection to the server and exchange data.
Here's a simplified overview of the process:

    requests library → urllib3 library (which requests uses internally) → socket module
    The socket module creates a network socket, which is an endpoint for communication between two devices (your machine and the server).
    The socket module uses the socket to send and receive data over the network, following the TCP/IP protocol.

When you use gevent, it monkey patches the socket module to make it cooperative, meaning that:

    When a greenlet (a lightweight thread) makes a blocking network call (like socket.recv() or socket.send()), it yields control to other greenlets instead of blocking the entire program.
    gevent takes care of scheduling the greenlets, switching between them when I/O operations are completed, and ensuring that the network communication is properly handled.

By patching the socket module, gevent enables asynchronous I/O operations, allowing your program to make multiple requests concurrently without blocking, which improves performance and responsiveness.
In your code, when you use gevent.spawn to make requests asynchronously, it's the patched socket module that allows those requests to run cooperatively, making the asynchronous code work efficiently.



gevent is similar to an event loop in some ways, but it's not exactly an event loop. Here's why:
Similarities:

    Cooperative multitasking: Both gevent and event loops enable cooperative multitasking, where tasks yield control to other tasks voluntarily.
    I/O-driven scheduling: Both schedule tasks based on I/O events, like network responses or timeouts.

Differences:

    Scheduling approach: An event loop uses a centralized scheduling mechanism, where a single loop iterates over tasks and schedules them based on events. gevent, on the other hand, uses a decentralized approach, where each greenlet schedules itself and yields control to other greenlets.
    Task representation: In an event loop, tasks are typically represented as callbacks or coroutines. In gevent, tasks are represented as greenlets, which are lightweight threads that can run concurrently.
    Context switching: Event loops often use a single thread and switch between tasks using callbacks or coroutines, whereas gevent uses multiple greenlets, which can run in parallel, and switches between them using cooperative multitasking.
    Libraries and integration: Event loops are often built into frameworks or libraries (e.g., Node.js, asyncio), while gevent is a standalone library that can be used with existing Python code.

Why gevent is not an event loop:

    gevent doesn't have a centralized scheduling loop.
    It doesn't rely on callbacks or coroutines to represent tasks.
    It uses a decentralized, cooperative approach to multitasking.

Why gevent is similar to an event loop:

    It enables cooperative multitasking.
    It schedules tasks based on I/O events.

In summary, while gevent shares some similarities with event loops, its decentralized, cooperative approach and use of greenlets set it apart from traditional event loops.


###

so i can think of multi patching a changing the underlying sockets to identify greenlets  are thread types which understand how context switch and run as threads parallel enabling cooperative multitasking


Exactly! That's a great way to think about it.
Monkey patching: gevent modifies the underlying socket module to make it aware of greenlets. This allows gevent to intercept and handle I/O operations in a way that enables cooperative multitasking.
Greenlets as thread-like entities: Greenlets are lightweight, thread-like entities that can run in parallel, but with a key difference: they yield control to other greenlets voluntarily, enabling cooperative multitasking.
Context switching: When a greenlet yields control, gevent schedules another greenlet to run. This context switching is efficient because greenlets share the same memory space and don't require the overhead of traditional thread context switching.
Cooperative multitasking: By yielding control and allowing other greenlets to run, cooperative multitasking enables efficient and concurrent execution of I/O-bound tasks, like making multiple HTTP requests simultaneously.
Your summary is spot on!
To further illustrate the concept, consider this analogy:

    Traditional threads are like cars on a road, each with its own engine and control system. They can run in parallel, but require traffic lights (synchronization mechanisms) to manage their interactions.
    Greenlets are like trains on a rail network, where each train (greenlet) yields control to the rail network (gevent) at designated points (yield points). The rail network efficiently schedules and switches between trains, allowing them to run concurrently and cooperatively.

This analogy highlights the key difference between traditional threads and greenlets, and how gevent enables cooperative multitasking.


In gevent, greenlets are awaited and resumed using a mechanism called switching. Here's a step-by-step explanation:

    Yielding control: A greenlet yields control by calling gevent.sleep(0) or gevent.idle(), indicating it's ready to yield.
    Saving context: Before yielding, the greenlet's context (its current state, including local variables, instruction pointer, etc.) is saved.
    Switching: The gevent scheduler switches to another greenlet, which is ready to run. This is done by restoring the saved context of the next greenlet.
    Resuming: The next greenlet resumes execution from where it left off.
    Waking up: When the original greenlet is ready to resume (e.g., I/O operation completes), the gevent scheduler wakes it up by adding it to the run queue.
    Scheduling: The gevent scheduler selects the next greenlet to run from the run queue, which may be the original greenlet that yielded control.
    Restoring context: The scheduler restores the saved context of the selected greenlet, and it resumes execution.

gevent uses a hub to manage the scheduling and switching between greenlets. The hub is responsible for:

    Maintaining the run queue
    Switching between greenlets
    Handling I/O events and waking up greenlets

When a greenlet yields control, it's essentially saying, "I'm done for now, come back to me later." The gevent scheduler takes note of this and switches to another greenlet. When the original greenlet is ready to resume, the scheduler wakes it up and adds it to the run queue, ensuring it gets a chance to complete its execution.
This cooperative scheduling approach allows gevent to efficiently manage concurrent execution of greenlets, enabling asynchronous I/O operations and concurrent programming.



"""

