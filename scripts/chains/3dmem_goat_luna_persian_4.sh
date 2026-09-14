#!/usr/bin/env bash
set -uo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$SCRIPT_DIR"
source ~/anaconda3/etc/profile.d/conda.sh
conda activate 3dmem
mkdir -p logs
echo "[$(date)] START 3dmem_goat_luna_persian_4" | tee -a logs/3dmem_goat_luna_persian_4.log
CUDA_VISIBLE_DEVICES=4 python run_goatbench_evaluation.py \
  -cf cfg/local_3dmem_goat_luna.yaml \
  --start_ratio 0.125 --end_ratio 0.250 --split 1 \
  >> logs/3dmem_goat_luna_persian_4_eval.log 2>&1
echo "[$(date)] DONE exit=$?" | tee -a logs/3dmem_goat_luna_persian_4.log
