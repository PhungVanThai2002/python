import os
import os.path as osp

src_folder = 'C:/Users/Admin/Downloads/21_data_lan_3_Copy/21_data_lan_3/'

yolo_format = ['train', 'valid', 'test']

remove_list = []
count = 0
for i in yolo_format:
    label_folder = osp.join(src_folder, i, 'labels')
    for j in os.listdir(label_folder):
        full_path_label = osp.join(label_folder, j)
        with open(full_path_label, 'r') as file:
            # print(file.read())
            if file.read(1) == '2' or file.read(1)=='3':
                count=count+1
                # remove_list.append(full_path_label)
                # image_file_name = j[:-3] + 'jpg'
                # full_path_image = osp.join(src_folder, i, 'images', image_file_name)
                # remove_list.append(full_path_image)

print("========================="+"remove "+str(count)+"file labels and "+str(count)+" images")
# for i in remove_list:
#     os.remove(i)