"""This file show how to generate a QR Code using Python."""

import pyqrcode
from PIL import Image


def qrcode_generation(link):
    """Function for QR Code generation."""
    qr_code = pyqrcode.create(link)
    qr_code.png("QRCode.png", scale=5)
    Image.open("QRCode.png")

if __name__ == "__main__":
    link_qrcode = input("Enter anything to generate QR : ")
    qrcode_generation(link_qrcode)
