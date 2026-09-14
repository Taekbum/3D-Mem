"""
Aggregate per-split A-EQA result pkls/jsons (success_list_{s}_{e}.pkl, path_length_list_{s}_{e}.pkl,
gpt_answer_{s}_{e}.json, ...) in an output directory into the merged success_list.pkl,
path_length_list.pkl, gpt_answer.json, etc. -- without re-running the question loop.

Unlike GOAT-Bench's logger, this one doesn't log a success-rate summary at aggregate time
(success_list is just the list of succeeded question_ids, not a distance/spl metric) -- for
accuracy you still need evaluate-predictions.py + get-scores.py on the merged gpt_answer.json.

Logger.aggregate_results() only globs {output_dir}/{filename}_*.pkl|json and writes the merged
files; start_ratio/end_ratio/n_total_questions are only used by Logger.__init__ to preload one
specific split's pkl (which we don't need here), so they're passed as placeholders.

Usage:
    python aggregate_aeqa_results.py <output_dir>
"""
import argparse
import logging
import pickle

from src.logger_aeqa import Logger

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", help="experiment output directory, e.g. results/3dmem_aeqa_gpt56")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%H:%M:%S")

    logger = Logger(args.output_dir, start_ratio=0.0, end_ratio=1.0, n_total_questions=0, voxel_size=0.1)
    logger.aggregate_results()

    with open(f"{args.output_dir}/success_list.pkl", "rb") as f:
        success_list = pickle.load(f)
    logging.info(f"Total succeeded questions: {len(success_list)}")
