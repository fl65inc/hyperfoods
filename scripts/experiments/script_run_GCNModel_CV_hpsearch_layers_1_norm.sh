
echo 'EXPERIMENTS ISMB CV'


n_gcn_layers=1

python GCNModel_CV_hpsearch.py \
--out_dir 'out/gcnmodel/final_CV/layers_'$n_gcn_layers'/norm' \
--device_idx 1 \
--norm True \
--num_layers  $n_gcn_layers \
--hidden_gcn 8 \
--epochs 100

