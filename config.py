import configparser

confp = configparser.ConfigParser()
confp.read('config.ini', encoding='utf-8')
conf = confp['dev']

import logging
from logging.config import fileConfig

fileConfig('logging_config.ini')
