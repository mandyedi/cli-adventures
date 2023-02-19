import project as p

# TODO: DO NOT TEST game data json, use a schema validator if you want to test it
# TODO: use fixture for game data

PLACE_KEYS = [
    "place_id",
    "name",
    "visited",
    "text",
    "items",
    "next_place_ids"
]

def test_get_game_data():
    game_data = p.get_game_data("test_data.json")
    assert "places" in game_data.keys()
    place = game_data["places"][0]
    assert list(place.keys()) == PLACE_KEYS

def test_get_game_data_no_file():
    game_data = p.get_game_data("file_not_exists.json")
    assert game_data == {}

def test_available_actions():
    keys = p.ACTIONS.keys()
    assert "go" in keys
    assert "look" in keys
    assert "take" in keys
    assert "backpack" in keys
    assert "use" in keys
    assert "help" in keys
    assert "exit" in keys

def test_get_place_by_id():
    game_data = p.get_game_data("test_data.json")
    place = p.get_place_by_id("place_1", game_data)
    keys = place.keys()
    assert list(place.keys()) == PLACE_KEYS
