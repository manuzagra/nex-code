import pickle

from utils.image_utils import *
from utils.mpi_utils import get_similarity



# the one generated by gt
ground_truth = get_images('/mnt/home/users/tic_163_uma/manuzagra/output/exe_data_random-0_*/runs/evaluation/scene/rendered_val/images_IMG_0587.png_gt.png')[0]

single_model_image = get_images('/mnt/home/users/tic_163_uma/manuzagra/output/exe_data_random-0_*/runs/evaluation/scene/rendered_val/images_IMG_0587.png_ours.png')[0]

# get all the iamges except the ones from the experiment 0 (those are the ones without transformation)
multi_model_images = get_images('/mnt/home/users/tic_163_uma/manuzagra/output/exe_data_random-[1,2,3,4,5,6,7,8,9]*_*/runs/evaluation/scene/rendered_val/images_IMG_0587.png_ours.png')


## calculate the similarity of all of them

single_model = get_similarity(ground_truth, single_model_image)
single_model['image'] = single_model_image

# use pickle to save time in the debuging
try:
    with open('results/multi_model_list.pkl', 'rb') as f:
        multi_model_list = pickle.load(f)
except FileNotFoundError:
    print('Generating the data for the images.')
    multi_model_list = []
    for img in multi_model_images:
        multi_model = get_similarity(ground_truth, img)
        multi_model['image'] = img
        multi_model_list.append(multi_model)

    multi_model_list.sort(key=lambda x: x['SSIM'], reverse=True)

    with open('results/multi_model_list.pkl', 'wb') as f:
        pickle.dump(multi_model_list, f)


# now we are going to get some average images using different number of images
# as the list is sorted we will use always the images with better score
try:
    with open('results/av_multi_model_list.pkl', 'rb') as f:
        av_multi_model_list = pickle.load(f)
except FileNotFoundError:
    print('Generating the data for the average images.')
    av_multi_model_list = []
    for i in range(2, 20):
        imgs = [data['image'] for data in multi_model_list[:i]]
        img = average_image(imgs)
        
        av = get_similarity(ground_truth, img)
        av['image'] = img

        av_multi_model_list.append(av)

        with open('results/av_multi_model_list.pkl', 'wb') as f:
            pickle.dump(av_multi_model_list, f)

x = []
y_PSNR = []
y_SSIM = []
y_LPIPS = []
for i, data in enumerate(av_multi_model_list):
    x.append(i+2)
    y_PSNR.append(data['PSNR'])
    y_SSIM.append(data['SSIM'])
    y_LPIPS.append(data['LPIPS'])

single_model['PSNR'] = (single_model['PSNR'] - min(y_PSNR)) / (max(y_PSNR) - min(y_PSNR))
single_model['SSIM'] = (single_model['SSIM'] - min(y_SSIM)) / (max(y_SSIM) - min(y_SSIM))
single_model['LPIPS'] = (single_model['LPIPS'] - min(y_LPIPS)) / (max(y_LPIPS) - min(y_LPIPS))

x = np.array(x)
y_PSNR = (np.array(y_PSNR) - min(y_PSNR)) / (max(y_PSNR) - min(y_PSNR))
y_SSIM = (np.array(y_SSIM) - min(y_SSIM)) / (max(y_SSIM) - min(y_SSIM))
y_LPIPS = (np.array(y_LPIPS) - min(y_LPIPS)) / (max(y_LPIPS) - min(y_LPIPS))


import matplotlib.pyplot as plt
fig, ax = plt.subplots( nrows=1, ncols=1 )
ax.plot(x, y_PSNR, color='r', linestyle='dashdot')
ax.plot(x, y_SSIM, color='b', linestyle='dashdot')
ax.plot(x, y_LPIPS, color='g', linestyle='dashdot')

ax.axhline(single_model['PSNR'], color='r')
ax.axhline(single_model['SSIM'], color='b')
ax.axhline(single_model['LPIPS'], color='g')

ax.set_xlabel('Number of images used')
ax.set_ylabel('Similarity')

ax.set_xticks(range(min(x), max(x)+1, 1))

lgd = ax.legend(['PSNR', 'SSIM', 'LPIPS', 'PSNR reference', 'SSIM reference', 'LPIPS reference'], loc=7, bbox_to_anchor=(1.4,0.5))

fig.savefig('results/av_image.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.close(fig)
