import simplelogger
import sys
import os
import re

def test():
    assert True

class TestBasics(object):
    def test_output(self):
        logger = simplelogger.Logger(log_file="/Users/tayler/Documents/Programming/Python/simplelogger/tests/output")
        logger.log("test")
        last = get_last()
        last = last.split()
        assert last[-1] == "test"
        os.remove("/Users/tayler/Documents/Programming/Python/simplelogger/tests/output")


class TestLevels(object):
    def setup(self):
        self.l = simplelogger.Logger(log_file="/Users/tayler/Documents/Programming/Python/simplelogger/tests/output")
        self.l.log_format('{level}')

    def teardown(self):
        os.remove("/Users/tayler/Documents/Programming/Python/simplelogger/tests/output")

    def test_info(self):
        self.l.info("test")
        assert get_last() == "INFO\n"

    def test_debug(self):
        self.l.debug("test")
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


class TestFormat(object):
    def teardown(self):
        os.remove("/Users/tayler/Documents/Programming/Python/simplelogger/tests/output")

    def setup(self):
        self.l = simplelogger.Logger(log_file="/Users/tayler/Documents/Programming/Python/simplelogger/tests/output")
        self.l.log_format('{datetime} {date} {time} {level} {text}')

    def test_all(self):
        self.l.log("test")

        output = open("/Users/tayler/Documents/Programming/Python/simplelogger/tests/output").readlines()[-1]

        if re.match('([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{6} ){2}\S* \S*', output):
            assert True
        else:
            assert False


def get_last():
    output = open("/Users/tayler/Documents/Programming/Python/simplelogger/tests/output", 'r').readlines()
    return output[-1]
