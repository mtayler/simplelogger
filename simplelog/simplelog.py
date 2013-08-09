import datetime

logging = False

def start():
	global logging
	logging = True
	timestamp("Logging Started")

def end(exit_code=0, message=''):
	if logging:
		print "Exited with status: {code}. {msg}\n".format(code=exit_code, msg=message)

def stop():
	if logging:
		logging = False

def timestamp(message):
	if logging:
		print "{timestamp}: {message}".format(message=message, timestamp=datetime.datetime.now())
