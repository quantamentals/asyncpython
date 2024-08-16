"""
Databases are crucial and asyncio supports async db drivers to execute
queries concurrenlty, improving performance

Popular async drivers include:

    - AsyncPG (Postgres): pip install asyncpg
    - Motor (MongoDB): pip install motor
    - Aio_pika (RabbitMQ): pip install aio-pika
    - Asyncio Redis (Redis): pip install aioredis
    - aiosqlite (SQLite): pip install aiosqlite 
 """
import asyncio
import aiosqlite

async def main():
    async with aiosqlite.connect('database.db') as db:
        # Create a table
        await db.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')

        # Insert data
        await db.execute('INSERT INTO users (name) VALUES (?)', ('John Doe',))

        # Commit the transaction
        await db.commit()

        # Query data
        async with db.execute('SELECT * FROM users') as cursor:
            rows = await cursor.fetchall()
            for row in rows:
                print(row)


# creating async sql coroutines
async def fetch_data(db):
	async with db.execute("SELECT * FROM users") as cursor:

		rows = await cursor.fetchall()
		return rows

async def main():

	# aiosqlite provides the context manager or i could make a custom one
	# this makes sure that cursors are properly cleaned up with db connections
	async with aiosqlite.connect('database.db') as db:
		tasks = [fetch_data(db), fetch_data(db), fetch_data(db)]
		results = await asyncio.gather(*tasks)

	for result in results:
		for row in result:
			print(row)


async def create_table(db_name, table_name):
	async with aiosqlite.connect(db_name) as db:
		await db.execute(f'Create table if not exists {table_name}(id integer primary_key, message_text)')
		await db.commit()



async def insert_data(db_name, table_name, message):
	async with aiosqlite.connect(db_name) as db:
		await db.execute(f'insert into {table_name} (message_text) VALUES (?)',(message,))
		await db.commit()


async def fetch_data(db_name, table_name):
    async with aiosqlite.connect(db_name) as db:
        async with db.execute(f'SELECT id, message_text FROM {table_name}') as cursor:
            return [row async for row in cursor]

async def main():

	db_name = 'test.db'
	table_name = 'greetings'
	await create_table(db_name=db_name, table_name=table_name)
	await insert_data(db_name=db_name, table_name=table_name, message='Hello, Async101')

	greetings = await fetch_data(db_name=db_name, table_name=table_name)


	for greeting in greetings:
		print(f"Greeting {greeting[0]}: {greeting[1]}")


asyncio.run(main())	