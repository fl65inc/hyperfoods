
echo 'EXPERIMENTS ISMB CV'


n_gcn_layers=2

python GCNModelWPathways_CV_hpsearch.py \
--out_dir 'out/gcnmodelwpathways/final_CV/layers_'$n_gcn_layers'/norm' \
--device_idx 0 \
--norm True \
--num_layers  $n_gcn_layers \
--hidden_gcn 8 \
--epochs 100

