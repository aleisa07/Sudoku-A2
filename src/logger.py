import os
import logging
from singleton_meta_class import SingletonMetaClass


class LoggerManager(object):

    __metaclass__ = SingletonMetaClass

    def __init__(self, log_id_name, log_file_name="../sudoku.log"):
        """Constructor of Logger Manager

        Keyword arguments:
        log_file_name -- file name of the log

        """
        file_handler = self.get_file_handler(log_file_name)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger_name = log_id_name

    def get_file_handler(self, log_file_name):
        """The method will convert the log_file_name in a absolute path and Return the file handler
        of the log_file

        Keyword arguments:
        log_file_name -- file name of the log (i.e. sudoku.log)

        """
        self.log_file_abs_path = os.path.abspath(log_file_name)
        handler = logging.FileHandler(self.log_file_abs_path, 'a')
        return handler

    def error(self, msg):
        """Method that written in the log a text message of type error

        Keyword arguments:
        msg -- Message written in the log

        """
        self.logger = logging.getLogger(self.logger_name)
        self.logger.error(msg)

    def info(self, msg):
        """Method that written in the log a text message of type info

        Keyword arguments:
        msg -- Message written in the log

        """
        self.logger = logging.getLogger(self.logger_name)
        self.logger.info(msg)

    def get_log(self):
        """Return the content of the log"""
        open_file = open(self.log_file_abs_path, 'r')
        text = open_file.read()
        open_file.close()
        return str(text)

    def clear_log(self):
        """Clear the content of the log"""
        open_file = open(self.log_file_abs_path, 'w')
        open_file.close()