"""
File: mirror_lake.py
Name:Jason
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: filename
    :return: n_img
    """
    n_img = SimpleImage.blank(filename.width, filename.height*2)
    for x in range(filename.width):
        for y in range(filename.height):
            #  make original
            filename_p = filename.get_pixel(x, y)
            n_img_p = n_img.get_pixel(x, y)
            n_img_p.red = filename_p.red
            n_img_p.green = filename_p.green
            n_img_p.blue = filename_p.blue
            #   make mirror lake
            n_img_p2 = n_img.get_pixel(x, n_img.height-y-1)
            n_img_p2.blue = filename_p.blue
            n_img_p2.green = filename_p.green
            n_img_p2.red = filename_p.red
    return n_img


def main():
    """
    TODO:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect(original_mt)
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
