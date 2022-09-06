from sys import exists
import configparser
from barcode import Code128
from barcode.writer import ImageWriter


def get_config():
    config = configparser.ConfigParser()
    if not exists('settings.ini'):
        config['BARCODE'] = {
            'LAST_BARCODE': 0,
            'PREFIX': 'TEST'
        }

        with open('settings.ini', 'w') as configfile:
            config.write(configfile)

    config.read('settings.ini')
    return config


CONFIG = get_config()
LAST_BARCODE = CONFIG['BARCODE']['LAST_BARCODE']
BARCODE_PREFIX = CONFIG['BARCODE']['PREFIX']


def make_barcode_str(num):
    final_barcode = BARCODE_PREFIX + str('%06d' % num)
    return final_barcode


def write_new_last_num(num):
    config = configparser.ConfigParser()
    config.read('settings.ini')
    config['BARCODE']['LAST_BARCODE'] = str(num)
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)


def create_barcode(barcode_str, module_width,
                   module_height):
    writer = ImageWriter()
    options = {'module_width': module_width,
               'module_height': module_height,
               'text_distance': 0.6}
    with open('code.png', 'wb') as f:
        Code128(barcode_str, writer=writer).write(f, options=options)
