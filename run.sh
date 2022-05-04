root=$1
folder=$2

cd DROID-SLAM

echo "Running DROID-SLAM with normal RGB images (non-modified)"
python demo.py --imagedir=$root/$folder/rgb --calib=calib/tum3.txt

echo "Running DROID-SLAM with segmented image)"
python demo.py --imagedir=$root/$folder/removed --calib=calib/tum3.txt

echo "Running DROID-SLAM with inpainted image)"
python demo.py --imagedir=$root/$folder/processed/masks --calib=calib/tum3.txt
