#!/bin/bash
HOME=/home/pwolfe8
TF_FILES=$HOME/r2d2_identifier/tf_files

sudo python $HOME/tensorflow/tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir=$TF_FILES/bottlenecks \
--how_many_training_steps 500 \
--model_dir=$TF_FILES/inception \
--output_graph=$TF_FILES/retrained_graph.pb \
--output_labels=$TF_FILES/retrained_labels.txt \
--image_dir=$HOME/r2d2_identifier/training_data
