"""

When testing asynchronous code, we need to define test cases 
as async functions using async def syntax

The @pytest.mark.asyncio decorator is used to mark the test function as 
an async test case

Inside the test function we can call and await the coroutine being test

We can user asseertions to very the expected behavior of the coroutine

"""

import asyncio
import pytest


@pytest.mark.asyncio
async def test_my_coroutine():

	result = await my_coroutine()
	assert result == 42


async def my_coroutine():
	await asyncio.sleep(1)
	return 42