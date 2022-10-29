import json

import numpy as np
import matplotlib.pyplot as plt

from utils.image_utils import get_image


ground_truth_path = '/mnt/home/users/tic_163_uma/manuzagra/more_images/images_IMG_0587.png_gt.png'
images_path = [
    '/mnt/home/users/tic_163_uma/manuzagra/more_images/av_image_24-5-15-6-14-11-2-22-21_images_IMG_0587.png',
    '/mnt/home/users/tic_163_uma/manuzagra/more_images/images_IMG_0587.png_ours.png'
]


def get_name(path):
    return path.split('/')[-1].split('.')[0]

values = {}
for i, path in enumerate(images_path):
    gt = get_image(ground_truth_path)
    img = get_image(path)

    diff = np.abs(gt - img)

    values[path] = np.sum(diff)/(diff.size*255)

    diff_img = np.sum(diff, axis=2)/3

    plt.imsave(f"more_images/diff_{i}-{path.split('/')[-1]}", diff_img.astype(np.uint8)[:,:], cmap='gray')

with open(f"more_images/diffs.json", 'w') as f:
    json.dump(values, f)