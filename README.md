# Dynamic-DROID-SLAM

```
@article{teed2021droid,
  title={{DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras}},
  author={Teed, Zachary and Deng, Jia},
  journal={Advances in neural information processing systems},
  year={2021}
}
```


## Requirements

To run the code you will need ...
* Create the environment using the command and activate the environment
```Python
conda env create -f environment.yml
conda activate droidenv
```
* Install some build dependencies in DROID-SLAM
```Python
cd DROID-SLAM
python setup.py install
cd ..
```


## Demos

1. Download the TUM dataset Download the fr1 sequences from [TUM-RGBD](https://vision.in.tum.de/data/datasets/rgbd-dataset/download)
2. Run the following command to preprocess the input sequence
```Python
sh preprocess.sh <data_root_for_TUM_dataset> <folder_name_of_the_sequence>
```

2. Run the following command to visualize the results for all the three experimental settings one by one
```Python
sh run.sh <data_root_for_TUM_dataset> <folder_name_of_the_sequence>
```


## Acknowledgements
1. We used DROID-SLAM (https://github.com/princeton-vl/DROID-SLAM) as the baseline for many experiments
2. We also used lama (https://github.com/saic-mdal/lama) for inpainting
3. Data from [TartanAir](https://theairlab.org/tartanair-dataset/) was used to train our model. We additionally use evaluation tools from [evo](https://github.com/MichaelGrupp/evo) and [tartanair_tools](https://github.com/castacks/tartanair_tools).
