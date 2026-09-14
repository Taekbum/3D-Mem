#!/usr/bin/env bash
set -uo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$SCRIPT_DIR"
source ~/anaconda3/etc/profile.d/conda.sh
conda activate 3dmem
mkdir -p logs
echo "[$(date)] START 3dmem_goat_luna_dogi_7" | tee -a logs/3dmem_goat_luna_dogi_7.log
CUDA_VISIBLE_DEVICES=7 python run_goatbench_evaluation.py \
  -cf cfg/local_3dmem_goat_luna.yaml \
  --start_ratio 0.250 --end_ratio 0.375 --split 1 \
  >> logs/3dmem_goat_luna_dogi_7_eval.log 2>&1
echo "[$(date)] DONE exit=$?" | tee -a logs/3dmem_goat_luna_dogi_7.log
