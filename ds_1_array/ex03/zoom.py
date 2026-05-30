import numpy as np
from load_image import ft_load
from PIL import Image


def roi_ok(image:np.ndarray, roi:tuple) -> bool:
    if 0 <= roi[0] < roi[2] <= image.shape[1] and \
          0 <= roi[0] < roi[2] <= image.shape[1]:
        return True
    else:
        return False

def zoom_PIL():
    pass


def zoom_42(image:np.ndarray, roi:tuple):
    assert roi_ok(image, roi), \
        f"Region of interest {roi} out of {image.shape[0]}, {image.shape[1]})"
    arr_cropped = image[roi[1]:roi[3],roi[0]:roi[2]]
    im_cropped = Image.fromarray(arr_cropped)
    zoomed = im_cropped.resize((image.shape[1], image.shape[0]))
    zoomed.show()


def main():
    arr = ft_load("animal.jpeg")
    print("arr ",arr.shape)
    im = Image.fromarray(arr)
    print("img ", im.size)
    im.show()
    cropped = im.crop((400,400,800,800))
    print(f"New shape after slicing: {arr.shape} or ({arr.shape[0]}, {arr.shape[1]})")
    cropped.show()
    # print(ft_load("./folder/landscape"))
    # print(ft_load("./landscape.jpg"))
    # print(ft_load("landscape2.png"))
    zoom_42(arr, (400,400,800,800))


if __name__ == "__main__":
    main()