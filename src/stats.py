
import json
from pathlib import Path
import copy
DEFAULT = {
        "games_played": 0,
        "games_won": 0,
        "games_lost": 0,
        "games_tied": 0,

        "last_game": {
            "timestamp": None,
            "rounds_requested": 0,
            "rounds_won": 0,
            "rounds_lost": 0,
            "rounds_draw": 0,
            "result": None
        }
    }
FILE = "stats.json"
path = Path(FILE)


def load_json():
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def load_stats():
    if path.exists():
        return load_json()
    else:
        return default_stats()
        


def default_stats():
    stats = copy.deepcopy(DEFAULT)

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=4, ensure_ascii=False)

    return stats

def save_stats(stats):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=4, ensure_ascii=False)


def save_update_stats(match_stats, result):
    stats = load_stats()
    stats["last_game"] = match_stats
    stats["games_played"] += 1

    match result:
        case "W":
            stats["games_won"] += 1
        case "L":
            stats["games_lost"] += 1
        case "D":
            stats["games_tied"] += 1

    save_stats(stats)
    
