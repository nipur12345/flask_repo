import io
import logging

def get_string_io_logger(log_stringio_obj, logger_name):
	#create logger
	logger = logging.getLogger(logger_name)
	formatter = logging.Formatter("%(asctime)s %(levelname)s \t[%(filename)s:%(lineno)s - %(funcName)s()] %(message)s")
	logger.setLevel(logging.INFO)

	#add normal steam handler to display logs on screen
	io_log_handler = logging.StreamHandler()
	logger.addHandler(io_log_handler)

	#create stream handler and initialise it with string io buffer
	string_io_log_handler = logging.StreamHandler(log_stringio_obj)

	#add stream handler to logger
	logger.addHandler(string_io_log_handler)

	return logger

#create string i/o object as string buffer
log_stringio_obj = io.StringIO()

#create stream log handler with string i/o buffer
log_handler = logging.StreamHandler(log_stringio_obj)
logger = get_string_io_logger(log_stringio_obj, logger_name='my_s3_logger')

logger.info("this log goes to string i/o buffer....")

#get log from string i/o buffer
print("This is the logs stored in string i/o buffer:\n{0}".format(log_stringio_obj.getvalue()))
