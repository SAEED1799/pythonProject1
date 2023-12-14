# Suppose you're building a logging library for a web application that needs to keep
# track of all requests and responses. You want to use the Singleton pattern to ensure
# that there's only one instance of the logger class throughout the application

class Logger:
    _instance = None

    def __new__(cls):
        # Using __new__ to control the creation of instances
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
            # Initialize the logger instance here
            cls._instance.log_messages = []
        return cls._instance

    def log(self, message):
        # Add log messages to the log_messages list
        self.log_messages.append(message)

    def get_log_messages(self):
        return self.log_messages
