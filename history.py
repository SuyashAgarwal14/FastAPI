import json
import os
from threading import Lock

HISTORY_FILE = "prompt_history.json"
_history_lock = Lock()

def load_history():
    with _history_lock:
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

def save_history(history):
    with _history_lock:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
