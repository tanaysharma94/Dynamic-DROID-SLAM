root=$1
folder=$2
#Example call to the file
#python demo_seg.py /data/slam_project/TUM/dynamic/ rgbd_dataset_freiburg3_walking_halfsphere
#python demo_seg.py /data/slam_project/TUM/dynamic/ rgbd_dataset_freiburg3_walking_halfsphere
python demo_seg.py $root $folder
python demo_sub.py $root $folder