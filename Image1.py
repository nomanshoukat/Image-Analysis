import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import io
from skimage.measure import label, regionprops

image_path = "Desktop/images/Neraj/a.tif"
image = io.imread(image_path)
rows = (float(image.shape[0]))
row = rows * 0.89  # For cutting the bottom border of an image
row_int = int(row)
im = image[0:row_int, :]
fig, ax = plt.subplots(ncols=1, nrows=3, figsize=(20, 20))

ax[0].hist(im.flatten(), bins=256)
ax[0].set_xticks(np.arange(0, 256, 20))
ax[0].set_xlim([0, 256])

ax[1].imshow(im, cmap="gray")
ax[1].set_title('Cropped image')
ax[1].axis('off')

# threshold the image based on grayscale value
black = im < 124
white = im > 125
# def plot_color_overlay():
all_layers = np.zeros((im.shape[0],
                       im.shape[1], 3))

# define color of your choice for two regions
all_layers[black] = (0, 0, 0)
all_layers[white] = (1, 1, 1)
b = (all_layers)
ax[2].imshow(b, cmap="gray")
ax[2].set_title('Thresholded image')
ax[2].axis('off')

# read image.txt for searching Image pixel size for area measurement
with open(image_path, "r+", errors='ignore') as f:
    f_contents = f.readlines()
    word = 'Image Pixel Size'
    for lines in (f_contents):
        if word in lines:
            t = str(lines)
            c = t[19:25]
            h = float(c)
            # convertion factor for converting nm to microns**2
            b = (h/1000)**2

black = black.astype(int)
regionprops = skimage.measure.regionprops(black)
area = [regionprop.area for regionprop in regionprops]
x = np.array([area])
Area_of_black_region = x*b
print(f"area of black region: {Area_of_black_region} µm2")

white = white.astype(int)
regionprops = skimage.measure.regionprops(white)
area = [regionprop.area for regionprop in regionprops]
y = np.array([area])
Area_of_black_region = y*b
print(f"area of white region: {Area_of_black_region} µm2")
