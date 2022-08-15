import os
import sys
from dotenv import load_dotenv
from barcode import Code128
from barcode.writer import ImageWriter
from printing import print_barcode

load_dotenv()
LAST_BARCODE = int(os.getenv('LAST_BARCODE'))
BARCODE_PREFIX = os.getenv('BARCODE_PREFIX')


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
    with open('.env', 'r') as env:
        data = env.readlines()
    to_write = f'LAST_BARCODE={num}\n'
    data[0] = to_write
    with open('.env', 'w') as env:
        env.writelines(data)


def create_barcode(barcode_str):
    writer = ImageWriter()
    options = {'module_width': 0.3,
               'module_height': 6.0,
               'text_distance': 0.6}
    with open('code.png', 'wb') as f:
        Code128(barcode_str, writer=writer).write(f, options=options)


def main():
    num_to_print = check_args()
    last_num = LAST_BARCODE
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
