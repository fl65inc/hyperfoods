python model_run.py \
--model gcn \
--out_dir 'out_time_complexity/gcn/layers_1/raw' \
--device_idx 0 \
--norm False \
--num_layers  1 \
--hidden_gcn 8 \
--batch_size 2 \
--epochs 10 &
python model_run.py \
--model gcn \
--out_dir 'out_time_complexity/gcn/layers_2/raw' \
--device_idx 0 \
--norm False \
--num_layers  2 \
--hidden_gcn 8 \
--batch_size 2 \
--epochs 10 &
python model_run.py \
--model gcn \
--out_dir 'out_time_complexity/gcn/layers_3/raw' \
--device_idx 0 \
--norm False \
--num_layers  3 \
--hidden_gcn 8 \
--batch_size 2 \
--epochs 10 &
python model_run.py \
--model sage \
--out_dir 'out_time_complexity/sage/layers_1/raw' \
--device_idx 1 \
--norm False \
--num_layers  1 \
--hidden_gcn 8 \
--batch_size 2 \
--epochs 10 &
python model_run.py \
--model sage \
--out_dir 'out_time_complexity/sage/layers_2/raw' \
--device_idx 1 \
--norm False \
--num_layers  2 \
--hidden_gcn 8 \
--batch_size 2 \
--epochs 10 &
python model_run.py \
--model sage \
--out_dir 'out_time_complexity/sage/layers_3/raw' \
--device_idx 3 \
--norm False \
--num_layers  3 \
--hidden_gcn 8 \
--batch_size 2 \
--epochs 10 &
python model_run.py \
--model cheb \
--out_dir 'out_time_complexity/cheb/layers_1/raw' \
--device_idx 3 \
--norm False \
--num_layers  1 \
--hidden_gcn 8 \
--batch_size 2 \
--epochs 10 &
python model_run.py \
--model cheb \
--out_dir 'out_time_complexity/cheb/layers_2/raw' \
--device_idx 3 \
--norm False \
--num_layers  2 \
--hidden_gcn 8 \
--batch_size 2 \
--epochs 10 &
python model_run.py \
--model cheb \
--out_dir 'out_time_complexity/cheb/layers_3/raw' \
--device_idx 3 \
--norm False \
--num_layers  3 \
--hidden_gcn 8 \
--batch_size 2 \
--epochs 10 &