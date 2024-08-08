
"""

Context managers are used to perform some required action after we have done something

exp. close file after writing to it


Context managers are possible because of magic methods __enter__() and __exit__()



"""


# what is an asyncronous context manager



# non context manager way
try: 

	file = open('filename.txt', 'w')
	file.write('hello world!')

except IOError:
	print("Unable to create file on disk")

finally:
	file.close()


# A Generic Context Manager


class GenericContextManager:


	def __init__(self, obj):
		self.obj = obj


	def __enter__(self):
		"""This method should return the context"""
		return self.obj


	def __exit__(self, exception_type, exception_value, traceback):
		if self.obj:
			self.obj.close()


# A file context manager implentation


class WriteToFile:


	def __init__(self, filename):
		self.filename = filename


	def __enter__(self):
		self.file_obj = open(self.filename,'w')
		return self.file_obj


	def __exit__(self, exception_type, exception_value, traceback):
		if self.file_obj:
			self.file_obj.close()


def main():

	with WriteToFile('test.txt') as f:

		f.write('A context manager from scratch')


if __name__ == '__main__':
	main()