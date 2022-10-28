import glob

import numpy as np
import cv2

def average_image(images, shape=None):
    """
    Generate the averrage image of multiple images, if they have different shape it reshapes them to a desired resolution
    Args:
        images (list of np.array): list of images. The images will be of the type np.array
        shape (tuple(width, height)): is the desired size of the output image
    Returns:
        (np.array): average image with the given size
    """

    if shape is None:
        shape = images[0].shape

    final = np.zeros(shape, np.float)

    for img in images:
        if img.shape[:2] != shape[:2]:
            print(img.shape, shape)
            img = cv2.resize(img, dsize=shape)
        final += img
    
    return final/len(images)

def get_image(path):
    return cv2.imread(path)

def get_images(pathname):
    """
    pathname(str): can be either absolute or relative, and can contain shell-style wildcards. 
    """
    images = {}
    for img in glob.glob(pathname, recursive=True):
        images[img] = get_image(img)
    return images

def get_paths(pathname):
    paths = []
    for p in glob.glob(pathname, recursive=True):
        paths.append(p)
    return paths

def averrage_image_patter_file(pathname):
    images = get_images(pathname)
    return average_image(images)

def resize(image, shape):
    return cv2.resize(image, dsize=shape)