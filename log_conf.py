from os import makedirs
import logging
import logging.config


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default_formatter': {
            'format': '\n[%(levelname)s][%(asctime)s] %(message)s',
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default_formatter',
            'filename': '.logs/logs.log',
        },
    },
    'loggers': {
        'super_logger': {
            'handlers': ['file_handler'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
makedirs('.logs', exist_ok=True)
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('super_logger')
