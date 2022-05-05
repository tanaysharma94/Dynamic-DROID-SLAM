#!/bin/bash


TUM_PATH=/data/slam_project/TUM/dynamic/

evalset=(
    rgbd_dataset_freiburg3_walking_xyz
    
)

# rgbd_dataset_freiburg3_walking_xyz
#     rgbd_dataset_freiburg3_walking_rpy
#     rgbd_dataset_freiburg3_walking_static
#     rgbd_dataset_freiburg3_sitting_halfsphere
#     rgbd_dataset_freiburg3_sitting_xyz

for seq in ${evalset[@]}; do
    python evaluation_scripts/test_tum.py --datapath=$TUM_PATH/$seq --weights=droid.pth --disable_vis $@
done

