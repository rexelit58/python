import logging
logging.basicConfig(filename='log.txt',level=logging.WARNING)
print('logging module demo')
logging.debug('debug information')
logging.info('info information')
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')