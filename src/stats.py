
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


def validate_stats(stats, expected):
    if stats.keys() != expected.keys():
        return False

    for key in expected:
        expected_value = expected[key]
        actual_value = stats[key]

        if isinstance(expected_value, dict):
            if not isinstance(actual_value, dict):
                return False

            if not validate_stats(actual_value, expected_value):
                return False

    return True
    
    
    
def default_stats():
    stats = copy.deepcopy(DEFAULT)

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=4, ensure_ascii=False)

    return stats


def load_stats():
    if not path.exists():
        return default_stats()

    stats = load_json()

    if validate_stats(stats, default):
        return stats

    return default_stats()
        

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
    
