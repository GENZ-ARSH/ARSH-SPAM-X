import json
import os
from pathlib import Path
from typing import List, Set

SUDO_FILE = "data/sudo_users.json"

def ensure_data_dir():
    Path("data").mkdir(exist_ok=True)
    if not os.path.exists(SUDO_FILE):
        with open(SUDO_FILE, 'w') as f:
            json.dump({"sudo_users": []}, f)

def load_sudo_users() -> Set[int]:
    ensure_data_dir()
    try:
        with open(SUDO_FILE, 'r') as f:
            data = json.load(f)
            return set(data.get("sudo_users", []))
    except Exception as e:
        print(f"Error loading sudo users: {e}")
        return set()

def save_sudo_users(sudo_users: List[int]) -> bool:
    ensure_data_dir()
    try:
        with open(SUDO_FILE, 'w') as f:
            json.dump({"sudo_users": list(sudo_users)}, f)
        return True
    except Exception as e:
        print(f"Error saving sudo users: {e}")
        return False

def add_sudo_user(user_id: int) -> bool:
    sudo_users = load_sudo_users()
    if user_id in sudo_users:
        return False
    sudo_users.add(user_id)
    return save_sudo_users(list(sudo_users))

def remove_sudo_user(user_id: int) -> bool:
    sudo_users = load_sudo_users()
    if user_id not in sudo_users:
        return False
    sudo_users.remove(user_id)
    return save_sudo_users(list(sudo_users))

def is_sudo_user(user_id: int) -> bool:
    return user_id in load_sudo_users() 