from stats import load_json, default_json
from pathlib import Path
import copy

FILE = 'history.json'
path = Path(FILE)
DEFAULT = [{
    "timestamp": None,
    "rounds_requested": 0,
    "rounds_won": 0,
    "rounds_lost": 0,
    "rounds_draw": 0,
    "result": None
}]

default_json(DEFAULT, FILE)



