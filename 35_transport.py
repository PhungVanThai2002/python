import os
import os.path as osp
import shutil

yolo_format = ['train', 'valid', 'test']

src_folder = '33_data_lan_7_person_no_trailer'
dst_folder = '../data_11_preprocessing'

for i in yolo_format:
    for j in ['images', 'labels']:
        folder_gan_nhat = osp.join(src_folder, i, j)
        for k in os.listdir(folder_gan_nhat):
            shutil.copy(osp.join(folder_gan_nhat, k), dst_folder)