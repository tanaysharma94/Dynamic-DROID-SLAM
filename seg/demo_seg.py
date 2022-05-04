import torch
import os
import numpy as np
from tqdm import tqdm

import sys

# or any of these variants
model = torch.hub.load('pytorch/vision:v0.10.0', 'deeplabv3_resnet101', pretrained=True)
#model = torch.hub.load('pytorch/vision:v0.10.0', 'deeplabv3_mobilenet_v3_large', pretrained=True)
model.eval()

# move the input and model to GPU for speed if available
if torch.cuda.is_available():
    device = torch.device('cuda:0')
else:
    device = torch.device('cpu')

model.to(device)

from PIL import Image
from torchvision import transforms

preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])


def mask_and_save(data_root, folder):
    
    path_to_imgs = os.path.join(data_root, folder, "rgb")
    save_path = os.path.join(data_root, folder, "masks")

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    image_paths = os.listdir(path_to_imgs)

    with torch.no_grad():
        for local_im_path in tqdm(image_paths):
            global_im_path = os.path.join(path_to_imgs, local_im_path)
            g_im = Image.open(global_im_path)
            g_im = g_im.convert("RGB")
            g_tensor = preprocess(g_im).unsqueeze(0)
            g_tensor = g_tensor.to('cuda:0')

            output = model(g_tensor)['out'][0]

            output_predictions = output.argmax(0)
            # Select human
            output_predictions = (output_predictions==15).int()
            output_predictions = torch.where(output_predictions > 0, 1, 0) * 255.

            im = Image.fromarray(output_predictions.byte().cpu().numpy()).resize(g_im.size)

            g_save_path = os.path.join(save_path, local_im_path)
            im.save(g_save_path) 



if __name__ =='__main__':

    if(len(sys.argv)!=3):
        print("Usage : python demo_seg.py <data_root> <folder_name>")
        
    else:
        data_root = sys.argv[1]
        folder = sys.argv[2]
        mask_and_save(data_root, folder)