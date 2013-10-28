import simplelogger
import re
from nose.tools import *

class MockStream(object):
    def __init__(self):
        self.output = []
        self.buffer = ''

    def write(self,text):
        self.buffer = text

    def flush(self):
        self.output.append(self.buffer)

class NoWriteStream(object):
    def flush(self):
        pass

class NoFlushStream(object):
    def write(self,text):
        pass

class TestIO(object):
    @raises(AttributeError)
    def test_stream_with_no_write(self):
        no_write_stream = NoWriteStream()
        logger = simplelogger.Logger(stream=no_write_stream)

    @raises(AttributeError)
    def test_stream_with_no_flush(self):
        no_flush_stream = NoFlushStream()
        logger = simplelogger.Logger(stream=no_flush_stream)

    def test_file_as_stream(self):
        logger = simplelogger.Logger(stream="tests/log_file.log")
        logger.debug("test")

    def test_stream_as_stream(self):
        stream = MockStream()
        logger = simplelogger.Logger(stream=stream)

class TestBasics(object):
    def test_output(self):
        stream = MockStream()
        logger = simplelogger.Logger(stream=stream)
        logger.info("test")
        output = stream.output[-1].split()
        assert output[-1] == "test"

class TestLevels(object):
    def setup(self):
        self.stream = MockStream()
        self.l = simplelogger.Logger(stream=self.stream)
        self.l.set_format('{level}')

    def test_info(self):
        self.l.info("test")
        assert self.stream.output[-1] == "INFO\n"

    def test_debug(self):
        self.l.set_threshold("debug")
        self.l.debug("test")
        assert self.stream.output[-1] == "DEBUG\n"

    def test_warning(self):
        self.l.warning("test")
        assert self.stream.output[-1] == "WARNING\n"

    def test_error(self):
        self.l.error("test")
        print self.stream.output[-1]
        assert self.stream.output[-1] == "ERROR\n"

    def test_critical(self):
        self.l.critical("test")
        assert self.stream.output[-1] == "CRITICAL\n"

    def test_custom(self):
        self.l.log("custom","test")
        assert self.stream.output[-1] == "CUSTOM\n"

    def test_threshold(self):
        self.l.set_threshold("warning")
        self.l.info("test")
        self.l.warning("test")

        output = self.stream.output[-1]

        assert output != "INFO\n" and output == "WARNING\n"

        self.l.set_threshold("critical")
        self.l.log("custom","test")

        assert self.stream.output[-1] == "CUSTOM\n"

class TestFormat(object):
    def setup(self):
        self.stream = MockStream()
        self.l = simplelogger.Logger(stream=self.stream)
        self.l.set_format('{datetime} {date} {time} {level} {text}')

    def test_all(self):
        self.l.info("test")

        output = self.stream.output[-1]

        if re.match('([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{6} ){2}\S* \S*', output):
            assert True
        else:
            assert False
