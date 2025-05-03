import json
from app.config import SECRETS_FILE


def get_flag(task_id):
    with open(SECRETS_FILE) as f:
        data = json.load(f)
    for item in data:
        if item["task_id"] == task_id:
            return item["flag"]
    return None
