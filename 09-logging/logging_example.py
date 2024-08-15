import logging
import time
import os

log_file_path = os.path.join(os.path.dirname(__file__), 'test_log.log')

logger = logging.getLogger('logAPP')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(log_file_path)

console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

def main():
    logger.debug('Debugging mode activated')
    logger.info('Application started')
    
    try:
        logger.info('Performing some operations...')
        for i in range(5):
            logger.debug(f'Operation {i+1} in progress')
            time.sleep(1)
        
        if True:
            logger.warning('This is a warning message')
        
        raise ValueError('An example error occurred')
    
    except ValueError as e:
        logger.error(f'Error encountered: {e}', exc_info=True)
    
    logger.info('Application finished')

if __name__ == '__main__':
    main()
