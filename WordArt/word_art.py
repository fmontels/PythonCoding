"""This file show how to make word art from image using Python."""

import pywhatkit

if __name__ == "__main__":
    img_path = input("Enter image to convert to Word Art :")
    pywhatkit.image_to_ascii_art(img_path, "MyArt")
