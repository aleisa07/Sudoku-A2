import os
import logging
from singleton_meta_class import SingletonMetaClass


class LoggerManager(object):

    __metaclass__ = SingletonMetaClass

    def __init__(self, player_name, logger_file="../sudoku.log"):
        """Constructor of Logger Manager

        Keyword arguments:
        logger_file -- file name of the log

        """
        file_handler = self.get_file_handler(logger_file)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger_name = player_name

    def get_file_handler(self, logger_file):
        """Return the file handler of the log

        Keyword arguments:
        logger_file -- file name of the log

        """
        self.log_file_name = os.path.abspath(logger_file)
        handler = logging.FileHandler(self.log_file_name, 'a')
        return handler

    def error(self, msg):
        """Method that written in the log a message of type error

        Keyword arguments:
        msg -- Message written in the log

        """
        self.logger = logging.getLogger(self.logger_name)
        self.logger.error(msg)

    def info(self, msg):
        """Method that written in the log a message of type info

        Keyword arguments:
        msg -- Message written in the log

        """
        self.logger = logging.getLogger(self.logger_name)
        self.logger.info(msg)

    def get_log(self):
        """Return the content of the log"""
        text = ""
        self.open_file = open(self.log_file_name, 'r')
        text = self.open_file.read()
        self.open_file.close()
        return str(text)

    def clear_log(self):
        """Clear the content of the log"""
        self.open_file = open(self.log_file_name, 'w')
        self.open_file.close()