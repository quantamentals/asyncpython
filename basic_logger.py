import logging 



class CustomLogger:


	def __init__(self,name):

		log_level = logging.DEBUG
		log_format = "%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s"

		self.logger = logging.getLogger(name)
		self.logger.setLevel(log_level)

		formatter = logging.Formatter(log_format)

		console_handler = logging.StreamHandler()
		console_handler.setFormatter(formatter)
		self.logger.addHandler(console_handler)



	def get_logger(self):
		return self.logger



def main():

	logger = CustomLogger(__name__).get_logger()
	logger.info('This is an info message')
	logger.debug('This is an debug message')
	logger.error('This is an error message')

if __name__ == '__main__':
	main()

