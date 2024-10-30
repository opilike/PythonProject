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
    for x in range(img.width):
        for y in range(img.height):
            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            red = 0
            blue = 0
            green = 0
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                # 0,0 0,1 1,0 1,1
                new_img_p = new_img.get_pixel(x, y)
                for i in range(2):
                    for j in range(2):
                        img_p = img.get_pixel(i, j)
                        blue += img_p.blue
                        red += img_p.red
                        green += img_p.green
                avg_b = blue // 4
                avg_r = red // 4
                avg_g = green // 4
                new_img_p.blue = avg_b
                new_img_p.green = avg_g
                new_img_p.red = avg_r
            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                new_img_p = new_img.get_pixel(x, y)
                for i in range(img.width-2, img.width):
                    for j in range(2):
                        img_p = img.get_pixel(i, j)
                        blue += img_p.blue
                        red += img_p.red
                        green += img_p.green
                avg_b = blue // 4
                avg_r = red // 4
                avg_g = green // 4
                new_img_p.blue = avg_b
                new_img_p.green = avg_g
                new_img_p.red = avg_r
            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                new_img_p = new_img.get_pixel(x, y)
                for i in range(2):
                    for j in range(img.height-2, img.height):
                        img_p = img.get_pixel(i, j)
                        blue += img_p.blue
                        red += img_p.red
                        green += img_p.green
                avg_b = blue // 4
                avg_r = red // 4
                avg_g = green // 4
                new_img_p.blue = avg_b
                new_img_p.green = avg_g
                new_img_p.red = avg_r
            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                new_img_p = new_img.get_pixel(x, y)
                for i in range(img.width-2, img.width):
                    for j in range(img.height-2, img.height):
                        img_p = img.get_pixel(i, j)
                        blue += img_p.blue
                        red += img_p.red
                        green += img_p.green
                avg_b = blue // 4
                avg_r = red // 4
                avg_g = green // 4
                new_img_p.blue = avg_b
                new_img_p.green = avg_g
                new_img_p.red = avg_r
            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)
                new_img_p = new_img.get_pixel(x, y)
                for i in range(x-1, x+2):
                    for j in range(2):
                        img_p = img.get_pixel(i, j)
                        blue += img_p.blue
                        red += img_p.red
                        green += img_p.green
                avg_b = blue // 6
                avg_r = red // 6
                avg_g = green // 6
                new_img_p.blue = avg_b
                new_img_p.green = avg_g
                new_img_p.red = avg_r
            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                new_img_p = new_img.get_pixel(x, y)
                for i in range(x - 1, x + 2):
                    for j in range(img.height-2, img.height):
                        img_p = img.get_pixel(i, j)
                        blue += img_p.blue
                        red += img_p.red
                        green += img_p.green
                avg_b = blue // 6
                avg_r = red // 6
                avg_g = green // 6
                new_img_p.blue = avg_b
                new_img_p.green = avg_g
                new_img_p.red = avg_r
            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)
                new_img_p = new_img.get_pixel(x, y)
                for i in range(2):
                    for j in range(y-1, y+2):
                        img_p = img.get_pixel(i, j)
                        blue += img_p.blue
                        red += img_p.red
                        green += img_p.green
                avg_b = blue // 6
                avg_r = red // 6
                avg_g = green // 6
                new_img_p.blue = avg_b
                new_img_p.green = avg_g
                new_img_p.red = avg_r
            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)
                new_img_p = new_img.get_pixel(x, y)
                for i in range(img.width-2, img.width):
                    for j in range(y-1, y+2):
                        img_p = img.get_pixel(i, j)
                        blue += img_p.blue
                        red += img_p.red
                        green += img_p.green
                avg_b = blue // 6
                avg_r = red // 6
                avg_g = green // 6
                new_img_p.blue = avg_b
                new_img_p.green = avg_g
                new_img_p.red = avg_r
            else:
                # Inner pixels.
                new_img_p = new_img.get_pixel(x, y)
                for i in range(x-1, x+2):
                    for j in range(y-1, y+2):
                        img_p = img.get_pixel(i, j)
                        blue += img_p.blue
                        red += img_p.red
                        green += img_p.green
                avg_b = blue // 9
                avg_r = red // 9
                avg_g = green // 9
                new_img_p.blue = avg_b
                new_img_p.green = avg_g
                new_img_p.red = avg_r
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
