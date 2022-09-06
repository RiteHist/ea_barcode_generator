import sys
import configparser
from os.path import exists
from barcode import Code128
from barcode.writer import ImageWriter
from printing import print_barcode


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


def check_args():
    if len(sys.argv) < 2:
        print('Usage: ea_barcode.py [number to print]')
        sys.exit()
    num_to_print = sys.argv[1]
    if not num_to_print.isdigit():
        print('Usage: ea_barcode.py [number to print]')
        sys.exit()
    return int(num_to_print)


def make_barcode_str(num):
    final_barcode = BARCODE_PREFIX + str('%06d' % num)
    return final_barcode


def write_new_last_num(num):
    config = configparser.ConfigParser()
    config.read('settings.ini')
    config['BARCODE']['LAST_BARCODE'] = str(num)
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)


def create_barcode(barcode_str):
    writer = ImageWriter()
    options = {'module_width': 0.3,
               'module_height': 6.0,
               'text_distance': 0.6}
    with open('code.png', 'wb') as f:
        Code128(barcode_str, writer=writer).write(f, options=options)


def main():
    num_to_print = check_args()
    last_num = int(LAST_BARCODE)
    try:
        for _ in range(num_to_print):
            last_num += 1
            barcode_str = make_barcode_str(last_num)
            create_barcode(barcode_str)
            print(barcode_str)
            print_barcode('code.png')
            write_new_last_num(last_num)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    main()
