import os
import os.path as osp

src_folder = 'xuly_11/data_11_preprocessing'

a = []

instance_car = 0

for i1 in os.listdir(src_folder):
    if i1.endswith(".txt"):
        full_path_txt = osp.join(src_folder, i1)
        with open(full_path_txt) as file:
            lines_in_file = file.readlines()
            number_lines = len(lines_in_file)
            count_lines_lane = 0
            for i2 in lines_in_file:
                info_in_line = i2.strip().split()
                if info_in_line[0] == '1':
                    count_lines_lane += 1
            if count_lines_lane == number_lines:
                a.append(full_path_txt)
                instance_car += count_lines_lane

print(len(a))
print(instance_car)

# for i in a:
#     png_path = i[:-3] + 'png'
#     jpg_path = i[:-3] + 'jpg'
#     os.remove(i)
#     if osp.exists(png_path):
#         os.remove(png_path)
#     elif osp.exists(jpg_path):
#         os.remove(jpg_path)