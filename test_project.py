import game as g

PLACE_KEYS = [
    "name",
    "visited",
    "text",
    "items",
    "interactables",
    "adjacent_places"
]

def test_get_game_data():
    game_data = g.get_game_data("data_test.json")
    place = game_data.places[0]
    assert place.name == "startplace"

def test_get_game_data_no_file():
    game_data = g.get_game_data("file_not_exists.json")
    assert game_data == {}

def test_available_actions():
    keys = g.ACTIONS.keys()
    assert "go" in keys
    assert "look" in keys
    assert "take" in keys
    assert "backpack" in keys
    assert "notes" in keys
    assert "use" in keys
    assert "help" in keys
    assert "exit" in keys

def test_get_place_by_name():
    game_data = g.get_game_data("data_test.json")
    place = g.get_place_by_name("place2", game_data)
    assert place is not None
