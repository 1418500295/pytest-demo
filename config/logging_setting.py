from logging.config import fileConfig
import os
import logging

class LogConfig():

    @staticmethod
    def get_logger():
        file_log = os.path.join(os.path.dirname(os.path.abspath(__file__)),"logging.ini")
        logging.config.fileConfig(file_log)
        logger = logging.getLogger(name="myAutoTest")
        return logger

if __name__ == '__main__':
    logger = LogConfig.get_logger()
    logger.info("ceshi")