#!/usr/bin/env bash
set -uo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$SCRIPT_DIR"
source ~/anaconda3/etc/profile.d/conda.sh
conda activate 3dmem
mkdir -p logs
echo "[$(date)] START 3dmem_aeqa_luna_persian_2" | tee -a logs/3dmem_aeqa_luna_persian_2.log
CUDA_VISIBLE_DEVICES=2 python run_aeqa_evaluation.py \
  -cf cfg/local_3dmem_aeqa_luna.yaml \
  --start_ratio 0.0 --end_ratio 0.5 \
  >> logs/3dmem_aeqa_luna_persian_2_eval.log 2>&1
echo "[$(date)] DONE exit=$?" | tee -a logs/3dmem_aeqa_luna_persian_2.log
