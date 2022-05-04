data_root=$1
folder=$2
export TORCH_HOME=$(pwd) && export PYTHONPATH=.
python3 bin/predict.py model.path=$(pwd)/big-lama indir=$data_root/$folder outdir=$data_root/$folder/processed