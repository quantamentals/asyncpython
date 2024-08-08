"""
Coroutines are based on generators internally

They can take args and return values

We can call coroutines from other coroutines

Coroutines can call regular functions but not vice versa


Coroutines are executed via an event loop.

We can only have one eventloop per thread

There are asycio methods for working with the event loop


Await takes another coroutine or another awaitable object

Awaitable objects implement __await__()

Await can only be used within coroutine functions

Await can only be used to call coroutines

Await starts the execution of the coroutine passed as an arguement

Await suspends the execution of the coroutine for which its is used


"""
async def f():
	return 1

print(type(f))

import inspect

print(inspect.iscoroutinefunction(f))


def g():
	yield 1

print(type(g))

gen = g()
print(type(gen))


coro = f()
print(type(coro))
print(inspect.iscoroutine(coro))

import asyncio
res = asyncio.run(coro) # we start the event loop with run



async def main():
	await asyncio.sleep(3)
	return 123



asyncio.run(main())