from win32 import win32print
import win32ui
from PIL import Image, ImageWin


HORZRES = 8
VERTRES = 10

LOGPIXELSX = 60
LOGPIXELSY = 70

PHYSICALWIDTH = 110
PHYSICALHEIGHT = 111

PHYSICALOFFSETX = 112
PHYSICALOFFSETY = 100


def print_barcode(filename):
    printer_name = win32print.GetDefaultPrinter()
    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC(printer_name)
    printable_area = hDC.GetDeviceCaps(HORZRES), hDC.GetDeviceCaps(VERTRES)
    printer_size = (hDC.GetDeviceCaps(PHYSICALWIDTH),
                    hDC.GetDeviceCaps(PHYSICALHEIGHT))

    png = Image.open(filename)
    ratios = [1 * printable_area[0] / png.size[0],
              0.6 * printable_area[1] / png.size[1]]
    scale = min(ratios)

    hDC.StartDoc(filename)
    hDC.StartPage()

    dib = ImageWin.Dib(png)
    scaled_width, scaled_height = [int(scale * i + 1) for i in png.size]
    x1 = int((printer_size[0] - scaled_width) / 2)
    y1 = int((printer_size[1] - scaled_height) / 2)
    x2 = x1 + scaled_width
    y2 = y1 + scaled_height

    dib.draw(hDC.GetHandleOutput(), (x1, y1, x2, y2))

    hDC.EndPage()
    hDC.EndDoc()
    hDC.DeleteDC()
