"""
File: fire.py
Name: Jason
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename:filename
    :return:filename
    """
    for x in range(filename.width):
        for y in range(filename.height):
            filename_pixel = filename.get_pixel(x, y)
            avg = (filename_pixel.red + filename_pixel.blue + filename_pixel.green)//3
            #  make HURDLE_FACTOR be fire pixel
            if filename_pixel.red > avg * HURDLE_FACTOR:
                filename_pixel.red = 255
                filename_pixel.blue = 0
                filename_pixel.green = 0
            #  else make grayscale
            else:
                filename_pixel.red = avg
                filename_pixel.blue = avg
                filename_pixel.green = avg

    return filename


def main():
    """
    TODO:
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires(original_fire)
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
