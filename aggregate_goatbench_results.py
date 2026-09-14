"""
Aggregate per-split GOAT-Bench result pkls (success_by_distance_{s}_{e}_{split}.pkl, etc.) in an
output directory into the merged success_by_distance.pkl / spl_by_distance.pkl / ... files, and log
the same "Total ... results: X, len: N" summary run_goatbench_evaluation.py prints at the end of a
run -- without re-running the scene loop.

Logger.aggregate_results() only globs {output_dir}/{filename}_*.pkl and writes the merged files;
start_ratio/end_ratio/split are only used by Logger.__init__ to preload one specific split's pkl
(which we don't need here), so they're passed as placeholders.

Usage:
    python aggregate_goatbench_results.py <output_dir>
"""
import argparse
import logging
import sys

from src.logger_goatbench import Logger

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", help="experiment output directory, e.g. results/3dmem_goatbench_gpt56")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%H:%M:%S")

    logger = Logger(args.output_dir, start_ratio=0.0, end_ratio=1.0, split=1, voxel_size=0.1)
    logger.aggregate_results()
