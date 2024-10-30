"""
File: stanCodoshop.py
Name: Jason
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
import math

from pandas.core.computation.common import result_type_many

from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    return math.sqrt((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    red_avg = 0
    green_avg = 0
    blue_avg = 0
    for i in range(len(pixels)):
        red_avg += pixels[i].red
        green_avg += pixels[i].green
        blue_avg += pixels[i].blue
    red = red_avg // len(pixels)
    green = green_avg // len(pixels)
    blue = blue_avg // len(pixels)
    return [red, green, blue]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    avg = get_average(pixels)
    min_d = float('inf')
    closest_pixel = None
    for pixel in pixels:
        dist = get_pixel_dist(pixel, avg[0], avg[1], avg[2])
        if dist < min_d:
            min_d = dist
            closest_pixel = pixel
    return closest_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    # green_im = SimpleImage.blank(20, 20, 'green')
    # green_pixel = green_im.get_pixel(0, 0)
    # print(get_pixel_dist(green_pixel, 5, 255, 10))
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0,0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # # print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))
    # best1 = get_best_pixel(([green_pixel, blue_pixel, blue_pixel]))
    for x in range(width):
        for y in range(height):
            # make collect_img [] make every img in one [] 找到每張圖片的其中一個像素，把它變成list
            collect_img = []
            for image in images:
                pixel = image.get_pixel(x, y)
                collect_img.append(pixel)
            #  make best_pixel to be a best_pixel
            best_pixel = get_best_pixel(collect_img)
            #  make best_pixel to be result_pixel
            result.pixel = result.get_pixel(x, y)
            result.pixel.red = best_pixel.red
            result.pixel.green = best_pixel.green
            result.pixel.blue = best_pixel.blue
    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
