import logging 

"""

Custom loggers serve several purposes:

    Flexibility: Custom loggers allow you to tailor logging to your specific application's needs, such as logging to different destinations (e.g., files, databases, or external services).
    Organization: You can create separate loggers for different modules or components within your application, making it easier to manage and filter log messages.
    Security: Custom loggers can be used to implement secure logging practices, such as encrypting log messages or logging sensitive information to a secure destination.
    Performance: Custom loggers can be optimized for performance-critical applications, reducing the overhead of logging.
    Integration: Custom loggers can be used to integrate with external logging systems or frameworks.

Use cases for custom loggers:

    Logging to multiple destinations: Create a custom logger that logs messages to both a file and a database.
    Filtering log messages: Create a custom logger that only logs messages above a certain level (e.g., only log errors and critical messages).
    Adding custom attributes: Create a custom logger that adds additional attributes to log messages, such as user IDs or request IDs.
    Implementing log message formatting: Create a custom logger that formats log messages in a specific way, such as adding timestamps or logging in JSON format.
    Creating a centralized logging system: Create a custom logger that aggregates log messages from multiple sources and logs them to a central location.

To use a custom logger, you typically:

    Create a custom logger class that inherits from logging.Logger or logging.Filter.
    Configure the custom logger with the desired settings (e.g., log level, format, destinations).
    Use the custom logger instance in your application code to log messages.

Example:
Python

# Create a custom logger that logs to a file and a database
class CustomLogger(logging.Logger):
    def __init__(self, name):
        super().__init__(name)
        self.file_handler = logging.FileHandler('log_file.log')
        self.db_handler = logging.handlers.SQLHandler('db_connection')
        self.addHandler(self.file_handler)
        self.addHandler(self.db_handler)

# Use the custom logger
logger = CustomLogger(__name__)
logger.info('This is a log message')

By using custom loggers, you can create a logging system that meets the specific needs of your application.

The log format syntax used in the code is:
"%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s"
This is a format string for the logging.Formatter class, which determines the layout of log messages. Here's a breakdown of each component:

    %(asctime)s:
        asctime refers to the timestamp of the log event.
        s indicates that the value should be formatted as a string.
        This will output the timestamp in the format YYYY-MM-DD HH:MM:SS,mmm (where mmm is milliseconds).
    %(levelname)s:
        levelname refers to the log level (e.g., INFO, DEBUG, ERROR, etc.).
        s indicates that the value should be formatted as a string.
        This will output the log level as a string (e.g., "INFO", "DEBUG", etc.).
    %(name)s:
        name refers to the logger name (in this case, the module name __name__).
        s indicates that the value should be formatted as a string.
        This will output the logger name as a string.
    %(funcName)s:
        funcName refers to the name of the function that logged the message.
        s indicates that the value should be formatted as a string.
        This will output the function name as a string.
    %(message)s:
        message refers to the actual log message.
        s indicates that the value should be formatted as a string.
        This will output the log message as a string.

The syntax %(key)s is used to insert the corresponding value into the format string. The key is a predefined attribute of the LogRecord object, and the s indicates the format type (in this case, a string).
When a log message is generated, the logging system replaces each %(key)s placeholder with the actual value, resulting in a formatted log message like this:
2024-08-18 14:30:00,000 - INFO - __main__ - main - This is an info message
Let me know if you have any further questions!

Yes, there are many other possibilities you can use in the log format string. Here are some examples:

    %(lineno)d: The line number of the log event.
    %(pathname)s: The full path of the file where the log event occurred.
    %(process)d: The process ID of the process that logged the event.
    %(processName)s: The name of the process that logged the event.
    %(thread)d: The thread ID of the thread that logged the event.
    %(threadName)s: The name of the thread that logged the event.
    %(module)s: The module name where the log event occurred.
    %(filename)s: The filename where the log event occurred.
    %(created)f: The time in seconds since the epoch when the log event was created.
    %(relativeCreated)d: The time in milliseconds since the logging system was initialized when the log event was created.
    %(msecs)d: The millisecond portion of the timestamp.
    %(levelno)d: The numeric log level (e.g., 10 for DEBUG, 20 for INFO, etc.).

You can also use custom attributes by passing them as extra arguments to the logging functions, like this:
Python

logger.info('This is an info message', extra={'custom_attribute': 'value'})

Then, you can include %(custom_attribute)s in your log format string to display the custom attribute.
Additionally, you can use various format specifiers to control the formatting of the values, such as:

    d: Integer value
    s: String value
    f: Floating-point value
    x: Hexadecimal value
    o: Octal value

For example:

    %(lineno)04d would format the line number as a four-digit integer with leading zeros.

Remember to consult the Python documentation for the logging module for a complete list of available attributes and format specifiers.


I'd be happy to explain!
What is a Handler?
In the context of Python's logging module, a Handler is an object that determines what happens to a log message after it's been generated. Handlers are responsible for:

    Outputting log messages to a destination, such as:
        Console (screen)
        File
        Network socket
        Database
        Email
        etc.
    Formatting log messages, if desired
    Filtering log messages based on criteria, such as log level or content

Console Handler
A Console Handler is a specific type of handler that outputs log messages to the console (screen). It's the most basic and common handler used in logging.
When you create a console handler, you can specify:

    Level: The minimum log level that will be output to the console (e.g., INFO, WARNING, ERROR, etc.)
    Formatter: The format of the log messages (e.g., timestamp, log level, message, etc.)
    Stream: The output stream (usually sys.stdout or sys.stderr)

Here's an example of creating a console handler:
Python

import logging

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Output INFO and above to console

# Create a formatter and attach it to the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the handler to a logger
logger = logging.getLogger(__name__)
logger.addHandler(console_handler)

Other Types of Handlers
Some other common handlers include:

    FileHandler: Outputs log messages to a file
    RotatingFileHandler: Outputs log messages to a file, rotating the file when it reaches a certain size
    TimedRotatingFileHandler: Outputs log messages to a file, rotating the file at a specified interval
    SocketHandler: Outputs log messages to a network socket
    SMTPHandler: Outputs log messages to an email address via SMTP

Each handler has its own configuration options and use cases. You can use multiple handlers to output log messages to different destinations, or use a single handler to output messages to a single destination.
Let me know if you have any further questions!


Yes, you can create custom handlers to output log messages to Redis, PubSub, or WebSockets. Here's a brief overview of each:
Redis Handler
A Redis handler can output log messages to a Redis instance, allowing you to store and analyze logs in a scalable and efficient manner. You can use the redis Python client library to create a custom handler.
Example:
Python

import logging
import redis

class RedisHandler(logging.Handler):
    def __init__(self, redis_host, redis_port, redis_db):
        self.redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

    def emit(self, record):
        self.redis_client.rpush('log_messages', self.format(record))

PubSub Handler
A PubSub handler can output log messages to a PubSub system, such as Redis PubSub or Google Cloud PubSub. This allows you to fan-out log messages to multiple subscribers.
Example (using Redis PubSub):
Python

import logging
import redis

class PubSubHandler(logging.Handler):
    def __init__(self, redis_host, redis_port, channel):
        self.redis_client = redis.Redis(host=redis_host, port=redis_port)
        self.channel = channel

    def emit(self, record):
        self.redis_client.publish(self.channel, self.format(record))

WebSocket Handler
A WebSocket handler can output log messages to a WebSocket endpoint, allowing you to stream logs to a web-based dashboard or client.
Example (using websockets library):
Python

import logging
import websockets

class WebSocketHandler(logging.Handler):
    def __init__(self, websocket_url):
        self.websocket_url = websocket_url

    async def emit(self, record):
        async with websockets.connect(self.websocket_url) as websocket:
            await websocket.send(self.format(record))

Note that these examples are simplified and might require additional configuration, error handling, and formatting to suit your specific use case.
To use these custom handlers, you'll need to add them to your logger instance, just like with built-in handlers:
Python

logger = logging.getLogger(__name__)
logger.addHandler(RedisHandler('localhost', 6379, 0))
logger.addHandler(PubSubHandler('localhost', 6379, 'log_channel'))
logger.addHandler(WebSocketHandler('ws://localhost:8765/logs'))

This way, you can output log messages to Redis, PubSub, or WebSockets, in addition to traditional destinations like files or consoles.



Here are some additional patterns and techniques that are useful with custom loggers:

    Contextual Logging: Use thread-local storage or other mechanisms to include contextual information (e.g., user ID, request ID) in log messages.
    Structured Logging: Use a structured format (e.g., JSON, key-value pairs) to log messages, making it easier to parse and analyze logs.
    Log Correlation: Use unique identifiers (e.g., correlation IDs) to correlate related log messages across different components or services.
    Log Sampling: Implement log sampling to reduce the volume of logs, especially in high-traffic systems.
    Log Sanitization: Sanitize sensitive information (e.g., passwords, credit card numbers) from log messages to ensure security and compliance.
    Log Routing: Route log messages to different destinations based on log level, component, or other criteria.
    Log Buffering: Buffer log messages in memory or a temporary storage to handle high-volume logging and reduce I/O overhead.
    Log Compression: Compress log messages to reduce storage space and network bandwidth.
    Log Encryption: Encrypt log messages to ensure confidentiality and security.
    Log Rotation: Rotate log files based on size, time, or other criteria to manage log storage and retention.
    Log Retention: Implement log retention policies to manage log storage and ensure compliance with regulations.
    Log Auditing: Audit log messages to detect and alert on security incidents, errors, or other critical events.
    Log Visualization: Visualize log data using dashboards, charts, or other tools to gain insights and monitor system behavior.
    Log Alerting: Set up alerts based on log messages to notify teams of critical events or errors.
    Log Integration: Integrate logs with other monitoring, analytics, or security tools to gain a comprehensive view of system behavior.

By applying these patterns and techniques, you can create a robust and effective logging system that provides valuable insights and helps you manage your application or system.

Here are some additional key concepts related to custom loggers that we might have missed:

    Async Logging: Logging messages asynchronously to improve performance and avoid blocking the main application thread.
    Log Queueing: Queueing log messages to handle high-volume logging and reduce I/O overhead.
    Log Batching: Batching log messages to reduce the number of I/O operations and improve performance.
    Log Message Enrichment: Enriching log messages with additional context or metadata to provide more insights.
    Log Data Transformation: Transforming log data into a different format or structure for easier analysis or storage.
    Log Data Normalization: Normalizing log data to a standard format to facilitate analysis and comparison.
    Log Anonymization: Anonymizing log data to protect sensitive information and ensure privacy.
    Log Data Retention and Purging: Managing log data retention and purging to ensure compliance with regulations and storage constraints.
    Log Security and Access Control: Implementing security measures and access controls to protect log data from unauthorized access.
    Log Monitoring and Alerting: Monitoring log data and setting up alerts to detect and respond to critical events or errors.
    Log Data Visualization and Analytics: Using data visualization and analytics tools to gain insights and understand log data.
    Log Integration with Other Tools: Integrating log data with other monitoring, analytics, or security tools to gain a comprehensive view of system behavior.
    Log Data Quality and Validation: Ensuring log data quality and validity to trust the insights and analysis.
    Log Scalability and Performance: Ensuring log handling can scale with the application and handle high volumes of log data without performance degradation.
    Log Compliance and Regulatory Requirements: Ensuring log handling meets compliance and regulatory requirements, such as GDPR, HIPAA, or PCI-DSS.

By considering these additional concepts, you can create a more comprehensive and effective logging system that meets your application's specific needs.

"""

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

