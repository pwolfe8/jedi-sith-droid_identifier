import os

commandstring='sudo python image_retraining/retrain.py \
--bottleneck_dir=tf_files/bottlenecks \
--how_many_training_steps 500 \
--model_dir=tf_files/inception \
--output_graph=tf_files/retrained_graph.pb \
--output_labels=tf_files/retrained_labels.txt \
--image_dir=training_images'

os.system(commandstring)
