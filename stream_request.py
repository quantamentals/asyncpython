import time 

import requests

s = requests.Session()


def generate_request():
	print('Sending first message')
	yield b'hi'

	print('Sleeping ......')
	time.sleep(5)

	print('Sending second message')

	yield b'there'


with requests.Session() as client:

	resp = client.post(f'http://{"127.0.0.1"}:{5000}',data=generate_request())
	print(resp, resp.text.strip())