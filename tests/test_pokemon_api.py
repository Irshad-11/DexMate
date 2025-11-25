# tests/test_pokemon_api.py
import pytest
from unittest.mock import patch, MagicMock
from src.pokemon_api import get_pokemon_data, suggest_names

# Sample minimal JSON shape returned by PokeAPI
SAMPLE_API_RESPONSE = {
    "name": "pikachu",
    "height": 4,
    "weight": 60,
    "types": [{"type": {"name": "electric"}}],
    "abilities": [{"ability": {"name": "static"}}, {"ability": {"name": "lightning-rod"}}],
    "stats": [
        {"stat": {"name": "hp"}, "base_stat": 35},
        {"stat": {"name": "attack"}, "base_stat": 55},
        {"stat": {"name": "defense"}, "base_stat": 40},
    ],
}

@patch("src.pokemon_api.requests.get")
def test_get_pokemon_data_success(mock_get):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = SAMPLE_API_RESPONSE
    mock_get.return_value = mock_resp

    data = get_pokemon_data("pikachu")
    assert data is not None
    assert data["name"] == "pikachu"
    assert "electric" in data["types"]
    assert "static" in data["abilities"]
    assert data["base_stats"]["hp"] == 35

@patch("src.pokemon_api.requests.get")
def test_get_pokemon_data_not_found(mock_get):
    mock_resp = MagicMock()
    mock_resp.status_code = 404
    mock_get.return_value = mock_resp

    data = get_pokemon_data("no-such-pokemon")
    assert data is None

def test_suggest_names_basic():
    s = suggest_names(prefix="p")
    assert isinstance(s, list)
    assert len(s) > 0
