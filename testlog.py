import os
import time
import logging

import config



def main():
    logger = logging.getLogger('helper')
    print(logger.handlers)
    logger.info('abaaba')


if __name__ == '__main__':
    main()