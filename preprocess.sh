root=$1
folder=$2

cd seg
./seg_script.sh $root $folder
cd ../lama
./run.sh $root $folder