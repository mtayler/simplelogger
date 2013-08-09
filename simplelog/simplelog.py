import datetime

class Logger(object):
    """Basic logging class"""
    
    def __init__(self):
        logging = False
    
    def start(self):
        global logging
        logging = True
        timestamp("Logging Started")

    def end(self, exit_code=0, message=''):
        if logging:
            print "Exited with status: {code}. {msg}\n".format(code=exit_code,
                                                               msg=message
                                                               )

    def stop(self):
        if logging:
            logging = False

    def timestamp(self, message):
        if logging:
            print "{timestamp}: {message}".format(message=message,
                                                  timestamp=datetime.datetime.now()
                                                  )