import asyncio
import ssl 
import subprocess


def generate_ssl_certificates():
	print('ran')
	# Generate private key
	subprocess.run(["openssl", "genrsa", "-out", "server.key", "2048"])

	# Generate Certificate Signing Request (CSR)
	subprocess.run(["openssl", "req", "-new", "-key", "server.key", "-out", "server.csr"])

	# Generate self-signed certificate
	subprocess.run(["openssl", "x509", "-req", "-days", "365", "-in", "server.csr", "-signkey", "server.key", "-out", "server.crt"])


async def handle_client_requests(reader, writer):
	data = await reader.read(1024)
	message = data.decode()
	print(f"recieved from client: {message}")

	response = "Hello from server"

	writer.write(response.encode())

	await writer.drain()

	writer.close()
	await writer.wait_closed()


async def main():

	server = await asyncio.start_server(handle_client_requests, 'localhost', 8888, ssl=ssl_context)

	async with server:
		await server.serve_forever()


if __name__ == '__main__':

	generate_ssl_certificates()


	ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
	ssl_context.load_cert_chain('server.crt', 'server.key')

	asyncio.run(main())	
