"""
File: blur.py
Name:Jason
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)
    # Loop over the picture
    for y in range(img.height):
        for x in range(img.width):
            red = 0
            blue = 0
            green = 0
            count = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x + i
                    pixel_y = y + j
                    if 0 <= pixel_x < img.width:
                        if 0 <= pixel_y < img.height:
                            img_p = img.get_pixel(pixel_x,  pixel_y)
                            blue += img_p.blue
                            red += img_p.red
                            green += img_p.green
                            count += 1
            new_img_p = new_img.get_pixel(x, y)
            new_img_p.red = red / count
            new_img_p.green = green / count
            new_img_p.blue = blue / count
    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
