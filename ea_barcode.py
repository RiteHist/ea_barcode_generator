import sys
import configparser
from os.path import exists

from barcode import Code128
from barcode.writer import ImageWriter

from printing import print_barcode


def get_config():
    """
    Loads config parameters from settings.ini file. If file doesn't
    exist, creates it and populates it with test parameters.
    Return ConfigParser object.
    """
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

def check_args():
    """
    Checks command line argument and if everything is corrects,
    returns the number of barcodes to print. Otherwise, prints command
    usage to stdout.
    """
    if len(sys.argv) < 2:
        print('Usage: ea_barcode.py [number to print]')
        sys.exit()
    num_to_print = sys.argv[1]
    if not num_to_print.isdigit():
        print('Usage: ea_barcode.py [number to print]')
        sys.exit()
    return int(num_to_print)


def make_barcode_str(prefix, num):
    """
    Creates a barcode string from prefix and the number preceded by zeroes.
    Returns final string.
    """
    final_barcode = prefix + str('%06d' % num)
    return final_barcode


def write_new_last_num(num):
    """
    Opens settings.ini file and replaces 'last_barcode' parameter with a new value.
    """
    config = configparser.ConfigParser()
    config.read('settings.ini')
    config['BARCODE']['LAST_BARCODE'] = str(num)
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)


def create_barcode(barcode_str):
    """Generates a Code 128 barcode and creates a .png image with it."""
    # TODO: pass dimensions of an image as parameters
    writer = ImageWriter()
    options = {'module_width': 0.25,
               'module_height': 6.0,
               'text_distance': 4.0}
    with open('code.png', 'wb') as f:
        Code128(barcode_str, writer=writer).write(f, options=options)

def send_to_print(num):
    num_to_print = num
    config = get_config()
    last_num = int(config['BARCODE']['LAST_BARCODE'])
    prefix = config['BARCODE']['PREFIX']
    try:
        for _ in range(num_to_print):
            last_num += 1
            barcode_str = make_barcode_str(prefix, last_num)
            create_barcode(barcode_str)
            print(barcode_str)
            print_barcode('code.png')
            write_new_last_num(last_num)
    except Exception as err:
        print(err)