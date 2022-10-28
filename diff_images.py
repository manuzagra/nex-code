import numpy as np
import matplotlib.pyplot as plt

from utils.image_utils import get_image


ground_truth_path = '/mnt/home/users/tic_163_uma/manuzagra/output/exe_data_random-0_2022-10-27_19:38:01/runs/evaluation/scene/rendered_val/images_IMG_0587.png_gt.png'
images_path = [
    '/mnt/home/users/tic_163_uma/manuzagra/output/exe_data_random-0_2022-10-27_19:38:01/runs/evaluation/scene/rendered_val/images_IMG_0587.png_ours.png',
    
]


def get_name(path):
    return path.split('/')[-1].split('.')[0]


for i, path in enumerate(images_path):
    gt = get_image(ground_truth_path)
    img = get_image(path)

    diff = np.sum(np.abs(gt - img), axis=2)/3

    plt.imsave(f"results/diff_{i}-{path.split('/')[-1]}", diff.astype(np.uint8)[:,:], cmap='gray')

