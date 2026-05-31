import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    inverted = 255 - array
    plt.imshow(Image.fromarray(inverted))
    plt.title("Figure VIII.2 Invert")
    plt.show()
    return inverted


def ft_red(array) -> np.ndarray:
    """Isolates red Channel, zeroing green and blue."""
    red = array.copy()
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    plt.imshow(Image.fromarray(red))
    plt.title("Figure VIII.3 Red")
    plt.show()
    return red


def ft_green(array) -> np.ndarray:
    """Isolates green Channel, zeroing red and blue."""
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    plt.imshow(Image.fromarray(green))
    plt.title("Figure VIII.4 Green")
    plt.show()
    return green


def ft_blue(array) -> np.ndarray:
    """Isolates blue Channel, zeroing red and green."""
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    plt.imshow(Image.fromarray(blue))
    plt.title("Figure VIII.5 Blue")
    plt.show()
    return blue


def ft_grey(array) -> np.ndarray:
    """Convert an RGB image to grayscale using luminance weights.

    Applies the ITU-R BT.601 luminance formula (0.299R + 0.587G + 0.114B)
    to produce a perceptually weighted grayscale image, displays it using
    matplotlib, and returns the result.

    Args:
        array: A NumPy array of shape (height, width, channels) representing
            an RGB or RGBA image. Only the first three channels are used.

    Returns:
        A 2D NumPy array of dtype uint8 containing the grayscale pixel
        values, with shape (height, width).
    """
    grey = np.dot(array[:, :, :3], [0.299, 0.587, 0.114]).astype(np.uint8)
    # grey is already a 2d-ndarray. does not requires Image.fromarray(grey)
    plt.imshow(grey, cmap='gray')
    plt.title("Figure VIII.6 Grey")
    plt.show()
    return grey
