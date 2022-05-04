import torch
import os
import numpy as np
from tqdm import tqdm
from PIL import Image, ImageOps
from torchvision import transforms
import cv2
import sys


def segment_and_save(data_root, folder):

    path_to_dir = os.path.join(data_root, folder)
    local_filenames = os.listdir(os.path.join(path_to_dir, 'masks'))
    preprocess = transforms.Compose([
        transforms.ToTensor(),
    ])

    for local_filename in tqdm(local_filenames):
        rgb_file = os.path.join(path_to_dir, 'rgb', local_filename)
        rgb = cv2.imread(rgb_file)
        
        mask_file = os.path.join(path_to_dir, 'masks', local_filename)
        mask = cv2.imread(mask_file, 0)
        
        rgb[mask > 0] = 0
        
        save_path = os.path.join(path_to_dir,'removed', local_filename)
        path = os.path.join(path_to_dir,'removed')
        if not os.path.exists(path):
            os.makedirs(path)
                
        cv2.imwrite(save_path, rgb)
    # assert False

if __name__ =='__main__':

    if(len(sys.argv)!=3):
        print("Usage : python demo_sub.py <data_root> <folder_name>")
        
    else:
        data_root = sys.argv[1]
        folder = sys.argv[2]
        segment_and_save(data_root, folder)
