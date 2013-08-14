import simplelogger
import sys
import os
import re


log_file = "/Users/tayler/Documents/Programming/Python/simplelogger/tests/output"

def test():
    assert True

class TestBasics(object):
    def test_output(self):
        global log_file
        self.log_file = log_file
        logger = simplelogger.Logger(log_file=self.log_file)
        logger.info("test")
        last = get_last()
        last = last.split()
        assert last[-1] == "test"
        os.remove(self.log_file)


class TestLevels(object):
    def setup(self):
        global log_file
        self.log_file = log_file
        self.l = simplelogger.Logger(log_file=self.log_file,threshold='debug')
        self.l.logging_format('{level}')

    def teardown(self):
        os.remove(self.log_file)

    def test_info(self):
        self.l.info("test")
        assert get_last() == "INFO\n"

    def test_debug(self):
        self.l.set_threshold("debug")
        self.l.debug("test")
        print open(self.log_file).read()
        assert get_last() == "DEBUG\n"

    def test_warning(self):
        self.l.warning("test")
        assert get_last() == "WARNING\n"

    def test_error(self):
        self.l.error("test")
        assert get_last() == "ERROR\n"

    def test_critical(self):
        self.l.critical("test")
        assert get_last() == "CRITICAL\n"

    def test_threshold(self):
        self.l.set_threshold("warning")
        self.l.info("test")
        self.l.warning("test")

        output = open(self.log_file).readlines()

        assert output[1] != "INFO\n" and output[1] == "WARNING\n"


class TestFormat(object):
    def teardown(self):
        os.remove(self.log_file)

    def setup(self):
        global log_file
        self.log_file = log_file
        self.l = simplelogger.Logger(log_file=self.log_file)
        self.l.logging_format('{datetime} {date} {time} {level} {text}')

    def test_all(self):
        self.l.info("test")

        output = open("/Users/tayler/Documents/Programming/Python/simplelogger/tests/output").readlines()[-1]

        if re.match('([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{6} ){2}\S* \S*', output):
            assert True
        else:
            assert False


def get_last():
    output = open("/Users/tayler/Documents/Programming/Python/simplelogger/tests/output", 'r').readlines()
    return output[-1]
