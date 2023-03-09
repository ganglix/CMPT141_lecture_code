# CMPT 141 - Arrays
# Topic(s): Array Applications
# DEMO


import numpy as np
import skimage.data as skdata
import matplotlib.pyplot as plt


def draw_histogram(image):
    """
    draw histogram data of 8-bit grayscale image to new figure
    image: 8-bit grayscale image to compute histogram for
    """

    # create 1D array of histogram data (maps intensities to counts)
    # 8-bit images have intensities from 0 to 255 inclusive
    # histogram = array of counts for intensity numbers

    # draw the histogram
    # plt.figure("Histogram")
    # plt.xlabel("Intensity")
    # plt.ylabel("Number of Pixels")
    # plt.bar(range(256), histogram)


# load image & draw image
image = skdata.camera()
plt.gray()
plt.imshow(image)
plt.show()
# compute & draw image's histogram
# draw_histogram(image)


# # display all figures
# plt.show()



#------------explore skills-----------
# things I want to mention

# histgram plot one-liner
# Can we modify this image?