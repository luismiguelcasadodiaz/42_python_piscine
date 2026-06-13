from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey
from PIL import Image
import matplotlib.pyplot as plt
...
array = ft_load("landscape.jpg")
print(f"The Shape of the image is: {array.shape}")
print(array)
print(ft_invert.__doc__)
plt.imshow(Image.fromarray(array))
plt.show()
invert = ft_invert(array)
red = ft_red(array)
green = ft_green(array)
blue = ft_blue(array)
grey = ft_grey(array)

fig, axes = plt.subplots(3, 2, figsize=(8, 12))

# axes is a 3×2 array, access like:
axes[0, 0].imshow(Image.fromarray(array))
axes[0, 0].set_title("Figure VIII.1: Original")
axes[0, 1].imshow(Image.fromarray(invert))
axes[0, 1].set_title("Figure VIII.2: Invert")
axes[1, 0].imshow(Image.fromarray(red))
axes[1, 0].set_title("Figure VIII.3: Red")
axes[1, 1].imshow(Image.fromarray(green))
axes[1, 1].set_title("Figure VIII.4: Green")
axes[2, 0].imshow(Image.fromarray(blue))
axes[2, 0].set_title("Figure VIII.5: Blue")
axes[2, 1].imshow(Image.fromarray(grey), cmap='gray')
axes[2, 1].set_title("Figure VIII.6: Grey")


# Optional: turn off axis ticks for cleaner look
for ax in axes.flat:
    ax.axis('off')

plt.tight_layout()
plt.show()
