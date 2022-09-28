"""This file show how to generate image captcha using Python."""

from captcha.image import ImageCaptcha


def captcha_generation(text):
    """Function for captcha generation."""
    img = ImageCaptcha(width=300, height=100)
    img.generate(text)
    img.write(text, "captcha.png")

if __name__ == "__main__":
    captcha_text = input('Enter Captcha text :')
    captcha_generation(captcha_text)
    