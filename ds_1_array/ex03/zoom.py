import numpy as np
from load_image import ft_load
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt


def roi_ok(im: np.ndarray, center: tuple) -> bool:
    """Check whether a center point falls within the bounds of an image.

    Validates that the given center coordinates lie within the spatial
    dimensions of the image array.

    Args:
        image: A NumPy array representing the image, with shape
            (height, width, ...).
        center: A tuple of (x, y) representing the point to validate.

    Returns:
        True if the center point is within the image boundaries,
        False otherwise.
    """
    return 0 <= center[0] <= im.shape[1] and 0 <= center[1] <= im.shape[0]


def z_coor(arr_range: tuple, center: tuple, factor: float) -> tuple:
    """Calculate zoom coordinates and dimensions relative to a center point.

    Computes a zoomed region within an array by scaling the original dimensions
    by the given factor, centering the result on the specified point, and
    clamping the boundaries to stay within the valid array range.

    Args:
        arr_range: A tuple of (height, width, channels) representing the
            dimensions of the source array.
        center: A tuple of (x, y) representing the center point of the
            zoom region.
        factor: The zoom factor. Values >= 1 shrink the region (zoom in),
            while values < 1 enlarge the region (zoom out).

    Returns:
        A tuple of (hei, wid, z_hei, z_wid, le, r, u, d) where:
            - hei: Original height of the array.
            - wid: Original width of the array.
            - z_hei: Height of the zoomed region.
            - z_wid: Width of the zoomed region.
            - le: Left boundary of the zoomed region (clamped to 0).
            - r: Right boundary of the zoomed region (clamped to wid).
            - u: Upper boundary of the zoomed region (clamped to 0).
            - d: Lower boundary of the zoomed region (clamped to hei).
    """
    hei, wid = arr_range[:2]  # grab only two dimensions

    if factor >= 1:
        z_hei = int(hei / factor)
        z_wid = int(wid / factor)
    else:
        z_hei = int(hei * factor)
        z_wid = int(wid * factor)
    left = center[0] - z_wid // 2
    righ = center[0] + z_wid // 2
    uppe = center[1] - z_hei // 2
    down = center[1] + z_hei // 2
    le = left if left >= 0 else 0
    r = righ if righ <= wid else wid
    u = uppe if uppe >= 0 else 0
    d = down if down <= hei else hei
    return (hei, wid, z_hei, z_wid, le, r, u, d)


def print_zoomed(im: Image):
    """Print the shape and pixel values of a PIL image as a 3D array.

    Converts the image to a NumPy array, expands it to three dimensions
    by adding a depth axis, then prints the resulting shape and the
    full array contents to stdout.

    Args:
        im: A PIL Image object, expected to be single-channel (e.g.,
            grayscale). Multi-channel images will already have a third
            dimension, making the added axis a fourth dimension, which
            may produce unexpected output.

    Note:
        This is a debugging/inspection utility. Printing the full array
        can produce very large output for non-trivial image sizes.
    """
    arr_im_2d = np.array(im)
    arr_im_3d = arr_im_2d[:, :, np.newaxis]
    z_hei, z_wid, z_dee = arr_im_3d.shape
    title = "New shape after slicing"
    print(f"{title}: ({z_hei}, {z_wid}, {z_dee}) or ({z_hei}, {z_wid})")
    print(arr_im_3d)


def zoom_PIL(im: np.ndarray, center: tuple, factor: int = 2):
    """Display a zoomed view of an image centered on a given point.

    Uses PIL to crop and resize (zoom in) or shrink and paste onto a
    transparent canvas (zoom out), then displays the result with matplotlib.

    Args:
        im    : A NumPy array representing the source image.
        center: A tuple of (x, y) specifying the focal point of the zoom.
        factor: The zoom factor. Values >= 1 crop the image around the
            center and upscale it (zoom in). Values < 1 downscale the
            image and place it on a transparent canvas (zoom out).
            Defaults to 2.

    Raises:
        AssertionError: If the center point lies outside the image
            boundaries, as determined by ``roi_ok``.

    See Also:
        z_coor: Computes the zoom region coordinates used by this function.
        roi_ok: Validates that the center point is within the image bounds.
    """
    assert roi_ok(im, center), \
        f"Center {center} out of {im.shape[0]}, {im.shape[1]})"
    hei, wid, z_hei, z_wid, l, r, u, d = z_coor(im.shape, center, factor)
    if factor >= 1:
        zoomed = Image.fromarray(im).crop((l, u, r, d)) \
                    .resize((wid, hei)).convert("L")
        print_zoomed(zoomed)
        plt.imshow(zoomed, cmap='gray', extent=(0, z_wid, z_hei, 0))
    else:
        canvas = Image.new("RGBA", (wid, hei), (0, 0, 0, 0))  # Transparent
        zoomed = Image.fromarray(im).resize((z_wid, z_hei)).convert("L")
        print_zoomed(zoomed)
        canvas.paste(zoomed)
        plt.imshow(canvas, extent=(0, wid, hei, 0))
    plt.show()


def zoom_42(image: np.ndarray, center: tuple, factor: float = 2.0):
    """Display a zoomed or shrunk image with labeled axes and tick marks.

    Renders the image onto a white canvas with a left and bottom axis,
    pixel-coordinate tick marks at intervals of 50, and a label indicating
    the zoom direction and factor. When zooming in (factor >= 1), the image
    is cropped around the center and upscaled; when zooming out (factor < 1),
    the entire image is downscaled. The result is displayed using PIL's
    built-in viewer.

    Args:
        image: A NumPy array representing the source image.
        center: A tuple of (x, y) specifying the focal point of the zoom.
        factor: The zoom factor. Values >= 1 crop around the center and
            upscale (zoom in). Values < 1 downscale the full image
            (zoom out). Defaults to 2.0.

    Raises:
        AssertionError: If the center point lies outside the image
            boundaries, as determined by ``roi_ok``.

    Note:
        Axis ticks reflect the coordinate space of the zoomed region
        when zooming in, or the original image coordinates when
        zooming out.

    See Also:
        z_coor: Computes the zoom region coordinates and dimensions.
        roi_ok: Validates that the center point is within the image bounds.
    """
    assert roi_ok(image, center), \
        f"Center {center} out of {image.shape[0]}, {image.shape[1]})"

    hei, wid, z_hei, z_wid, l, r, u, d = z_coor(image.shape, center, factor)
    x_zoom_ratio = wid / z_wid
    y_zoom_ratio = hei / z_hei
    # Create white background canvas bigger than original image
    margin = 60
    back_ground = Image.new("RGBA", (wid + margin, hei + margin),
                            (255, 255, 255, 255))  # White
    # set up drawing layer and put char title
    draw = ImageDraw.Draw(back_ground)
    label = ('Zoomed' if factor >= 1 else 'shrinked') + f" by {factor}"
    draw.text((5, hei + margin // 2), label, fill="red")
    draw.line((margin, 0, margin, hei), fill="black")
    draw.line((margin, hei, margin + wid, hei), fill="black")

    if factor >= 1:
        arr_cropped = image[u:d, l:r]
        im_cropped = Image.fromarray(arr_cropped).convert("L")
        zoomed = im_cropped.resize((wid, hei))
        print_zoomed(zoomed)
        for val in range(0, z_wid, 50):
            x = margin + int(val * x_zoom_ratio)
            y = hei + 5
            draw.text((x, y), str(val), fill="black",)
            draw.line((x, hei, x, y), fill="black")
        for val in range(0, z_hei, 50):
            y = int(val * y_zoom_ratio)
            draw.text((5, y), str(val), fill="black")
            draw.line((margin - 5, y, margin, y), fill="black")
    else:
        im_cropped = Image.fromarray(image).convert("L")
        zoomed = im_cropped.resize((z_wid, z_hei))
        print_zoomed(zoomed)
        # ticks and labels draw
        for val in range(0, wid, 50):
            x = margin + val
            y = hei + 5
            draw.text((x, y), str(val), fill="black")
            draw.line((x, hei, x, y), fill="black")
        for val in range(0, hei, 50):
            draw.text((5, val), str(val), fill="black")
            draw.line((margin - 5, val, margin, val), fill="black")

    back_ground.paste(zoomed, (margin, 0))
    back_ground.show()


def main():
    """Test zoom_42 and zoom_PIL with various zoom factors on animal.jpeg."""
    arr = ft_load("animal.jpeg")
    zoom_42(arr, (626, 460), 2)
    zoom_PIL(arr, (626, 460), 2)
    zoom_42(arr, (626, 460), 0.5)
    zoom_PIL(arr, (626, 460), 0.5)


if __name__ == "__main__":
    main()
