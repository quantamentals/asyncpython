"""
Testing protocols and network communication can be done usin AsyncIO streams


We can start test cases that starts a server with the protocol being tested


We then establish a client connection to the server using asyncio.open_connection()


The test case sends data to the server, reads the response, and asserts the expected behavior

The server is closed once test case is completed

Test fixtures are used to set up and tear down the environment before and after test cases

Fixtures are defined using @pytest.fixture decorator

The test cases tale tjt fixture as a parameter and uses it in the coroutine being tested

Setup code can be placed before the yield statement and teardown code can be placed after it



"""

import asyncio
import pytest
import pytest_asyncio

@pytest.mark.asyncio
async def test_my_protocol():
    server = await asyncio.start_server(my_protocol, "localhost", 0)
    _, port = server.sockets[0].getsockname()

    try:
        reader, writer = await asyncio.open_connection("localhost", port)
        writer.write(b"Hello, server!")
        await writer.drain()

        data = await reader.read(100)
        assert data == b'Hello, client!'
    finally:
        server.close()
        await server.wait_closed()

async def my_protocol(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    assert message == "Hello, server!"

    writer.write(b"Hello, client!")
    await writer.drain()
    writer.close()

@pytest.fixture(scope="module")
async def my_fixture():
    yield 42

async def my_coroutine(value):
    await asyncio.sleep(1)
    return value

@pytest.mark.asyncio
async def test_my_coroutine(my_fixture):
    async for fixture_value in my_fixture:
        result = await my_coroutine(fixture_value)
        assert result == 42



async def fetch_data():
	await asyncio.sleep(1)
	return {"data": 123}

@pytest.mark.asyncio
async def test_fetch_data():
	result = await fetch_data()
	assert result == {"data":123}, "Expected result did not match!"