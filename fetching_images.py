from math import pi
import os
import pickle



current_file_path = os.path.abspath(__file__)
parent_dir = os.path.dirname(current_file_path)
outer_dir = os.path.dirname(parent_dir)

image_data_folders = os.path.join(outer_dir, 'data', 'image_data','faces_0')
image_faces_folders = os.listdir(image_data_folders)



filenames = []

for folder in image_faces_folders:

    if folder.startswith('.'):
        continue
        
    for filename in os.listdir(os.path.join(image_data_folders, folder)):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            filenames.append(os.path.join(image_data_folders, folder, filename))


print("Total number of image files:", len(filenames))

pickle.dump(filenames, open(os.path.join(parent_dir, 'image_files.pkl'), 'wb'))