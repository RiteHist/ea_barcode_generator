from gui import init_gui


def main():
    """
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
    """
    init_gui()

if __name__ == '__main__':
    main()
