import json
import os
import pickle
from quaternion import as_float_array

if __name__ == "__main__":
    with open("data/open-eqa-v0.json", "r") as f:
        questions_list = json.load(f)

    hm3d_data_path = "/media/SSD2/tblee-larr/dataset/HM3D/data/scene_datasets/hm3d"

    aeqa_questions = []

    for question_data in questions_list:
        episode_history = question_data["episode_history"]
        dataset_name, scene_id = episode_history.split("/")
        dataset_name = dataset_name.split('-')[0]
        if dataset_name == "hm3d":
            scene_folder_identifier = scene_id.split('-')[-1] if '-' in scene_id else scene_id

            episodic_memory_path = os.path.join(hm3d_data_path, 'data', 'frames', 'hm3d-v0', scene_id)
            scene_memory_root = os.path.join(hm3d_data_path, 'val')
            for subfolder in os.listdir(scene_memory_root):
                subfolder_parts = subfolder.split('-')
                if len(subfolder_parts) >= 2 and subfolder_parts[1] == scene_folder_identifier:
                    scene_memory_path = subfolder
                    break

            pkl_files = sorted([os.path.join(episodic_memory_path, f) for f in os.listdir(episodic_memory_path) if f.endswith('.pkl')])
            with open(pkl_files[0], 'rb') as f:
                first_state = pickle.load(f)
            agent_state_first = first_state['agent_state']

            position = agent_state_first.position.tolist()
            # Get rotation quaternion from agent state and convert to list [w, x, y, z]
            rotation = as_float_array(agent_state_first.rotation).tolist()

            # Build the question entry
            question_entry = {
                "question": question_data["question"],
                "answer": question_data["answer"],
                "category": question_data["category"],
                "question_id": question_data["question_id"],
                "episode_history": scene_memory_path,
                "position": position,
                "rotation": rotation,
                "object_id": None,
                "class": None
            }

            # Add extra_answers if present in the original data
            if "extra_answers" in question_data:
                question_entry["extra_answers"] = question_data["extra_answers"]

            aeqa_questions.append(question_entry)

    # Save to file
    with open("data/aeqa_questions-557.json", "w") as f:
        json.dump(aeqa_questions, f, indent=4)

    print(f"Generated {len(aeqa_questions)} questions")