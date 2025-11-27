
import requests
from typing import Optional, Dict, Any

POKEAPI_BASE = "https://pokeapi.co/api/v2/pokemon/"


SUGGESTIONS = ["pikachu", "bulbasaur", "charmander", "squirtle", "eevee", "snorlax"]

def get_pokemon_data(name: str, timeout: float = 5.0) -> Optional[Dict[str, Any]]:
    """
    Fetch pokemon data from pokeapi. Returns parsed dict or None on not-found/error.
    """
    name = name.strip().lower()
    if not name:
        return None

    url = f"{POKEAPI_BASE}{name}"
    try:
        r = requests.get(url, timeout=timeout)
    except requests.RequestException:
        return None

    if r.status_code != 200:
        return None

    raw = r.json()

    data = {
        "name": raw.get("name"),
        "height": raw.get("height"),
        "weight": raw.get("weight"),
        "types": [t["type"]["name"] for t in raw.get("types", [])],
        "abilities": [a["ability"]["name"] for a in raw.get("abilities", [])],
        "base_stats": {s["stat"]["name"]: s["base_stat"] for s in raw.get("stats", [])},
    }
    return data

def suggest_names(prefix: Optional[str] = None, max_suggestions: int = 5):
    """
    Provide some suggested pokemon names. If prefix provided, filter suggestions.
    This is a cheap local suggestion list to avoid extra API calls.
    """
    prefix = (prefix or "").lower()
    filtered = [s for s in SUGGESTIONS if s.startswith(prefix)]
    if not filtered:
        filtered = SUGGESTIONS[:max_suggestions]
    return filtered[:max_suggestions]

# Sample edit for Demonstration