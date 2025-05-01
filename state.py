# tel_wp_sync/state.py
import json
from datetime import datetime
from pathlib import Path

STATE_FILE = Path("state.json")
DEFAULT_STATE = {
    "current": "green",
    "green": {
        "image": "green_light.jpg",
        "text": "Текст по умолчанию для зелёного"
    },
    "red": {
        "image": "red_light.jpg",
        "text": "Текст по умолчанию для красного"
    },
    "timer": ""
}

def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        save_state(DEFAULT_STATE)
        return DEFAULT_STATE.copy()

def save_state(data):
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_current_state():
    return load_state()["current"]

def get_text(color):
    return load_state()[color]["text"]

def set_state(color):
    state = load_state()
    if color in ["green", "red"]:
        state["current"] = color
        save_state(state)

def set_text(color, text):
    state = load_state()
    if color in ["green", "red"]:
        state[color]["text"] = text
        save_state(state)

def set_timer(timestamp):
    state = load_state()
    state["timer"] = timestamp
    save_state(state)

def get_timer():
    return load_state().get("timer", "")

def clear_timer():
    state = load_state()
    state["timer"] = ""
    save_state(state)

def check_timer_due():
    state = load_state()
    ts = state.get("timer")
    if not ts:
        return False
    try:
        dt = datetime.strptime(ts, "%Y-%m-%d %H:%M")
        return datetime.now() >= dt
    except:
        return False
