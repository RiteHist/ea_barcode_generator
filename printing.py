from win32 import win32print
import win32ui
from PIL import Image, ImageWin

# Windows constants for height and width in pixels
HORZRES = 8
VERTRES = 10

# Windows constants for physical width and height
PHYSICALWIDTH = 110
PHYSICALHEIGHT = 111


def print_barcode(filename):
    """
    Calculates the printing dimensions and sends a printing job of a given
    file to a system's default printer.
    """
    printer_name = win32print.GetDefaultPrinter()
    # Create uninitialised device context
    hDC = win32ui.CreateDC()
    # Creates a device context for a given printer
    hDC.CreatePrinterDC(printer_name)
    # Create a tuple of printable area by getting device parameters for
    # height and width in pixels
    printable_area = hDC.GetDeviceCaps(HORZRES), hDC.GetDeviceCaps(VERTRES)
    printer_size = (hDC.GetDeviceCaps(PHYSICALWIDTH),
                    hDC.GetDeviceCaps(PHYSICALHEIGHT))
    png = Image.open(filename)
    # Calculate how to scale an image: horizontally or vertically,
    # depending on the lowest x or y size of an image
    ratios = [1 * printable_area[0] / png.size[0],
              1 * printable_area[1] / png.size[1]]
    scale = min(ratios)
    hDC.StartDoc(filename)
    hDC.StartPage()

    dib = ImageWin.Dib(png)
    scaled_width, scaled_height = [int(scale * i + 1) for i in png.size]
    # Calculate the position of an image on printable area
    # TODO: pass margins as parameters and add them to calculations
    x1 = int((printer_size[0] - scaled_width) / 2)
    y1 = int((printer_size[1] - scaled_height) / 2)
    x2 = x1 + scaled_width
    y2 = y1 + scaled_height
    dib.draw(hDC.GetHandleOutput(), (x1, y1, x2, y2))

    hDC.EndPage()
    hDC.EndDoc()
    hDC.DeleteDC()
