import os

from .api import load_local_students


def load_students_dataset() -> list:
    # The dataset may live in the repo root (one level above the Streamlit project folder).
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    candidates = [
        os.path.join(project_root, "students_dataset.json"),
        os.path.join(project_root, "..", "students_dataset.json"),
    ]

    for candidate in candidates:
        candidate = os.path.abspath(candidate)
        if os.path.exists(candidate):
            return load_local_students(candidate)

    return []
