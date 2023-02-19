import json
from random import randint


game_run = True
backpack = []
notes = []
current_place = {}

PROMPT = ">:"
GAME_DATA = "data.json"

def print_interactables():
    for interactable in current_place["interactables"]:
        if interactable["taken"] is True:
            print(interactable["text_place_taken"])
        else:
            print(interactable["text_place"])

def print_items_around():
    global current_place
    if len(current_place["items"]) > 0:
        print("Collectible items around here:")
        for item in current_place["items"]:
            print(f"- {item['name']}")
    else:
        print("There isn't anything here to take. :(")


def print_places_around():
    global current_place
    if len(current_place["adjacent_places"]) > 0:
        print("Places to go from here:")
        for place in current_place["adjacent_places"]:
            print(f"- {place['name']}")
    else:
        print("You are trapped. There is no scape from here. :(")

def action_go(game_data, *args):
    global current_place
    if len(args) == 0:
        print("And how am I supposed to go nowhere?")
    else:
        if args[0] == current_place["name"]:
            print("You are exactly there.")
            return

        adjacent_places = [place["name"] for place in current_place["adjacent_places"]]
        if args[0] not in adjacent_places:
            print("I'm afraid this place is not around here.")
            return

        place = get_place_by_name(args[0], game_data)
        if place == None:
            print("And where the hell is this place?")
        else:
            current_place["visited"] = False
            current_place = place


def action_look(game_data, *args):
    if len(args) == 0:
        print("I can look at nothing, but only if I'm meditating.\n")
        return
    
    subject_to_look = args[0]

    # Handle current place
    if subject_to_look == "around":
        print_interactables()
        print("")
        print_items_around()
        print("")
        print_places_around()
        return

    # Handle place item
    for item in current_place["items"]:
        if item["name"] == subject_to_look:
            print(item["text"])
            return
    
    # Handle interactable
    global notes
    for interactable in current_place["interactables"]:
        if interactable["name"] == subject_to_look:
            if interactable["taken"] is True:
                print(interactable["text_look_taken"])
            else:
                print(interactable["text_look"])

            if len(interactable["required_item"]) == 0 and len(interactable["required_information"]) == 0:
                if len(interactable["item"]) > 0:
                    current_place["items"].append({"name": interactable["item"], "text": interactable["text_item"]})
                    interactable["item"] = ""
                    interactable["taken"] = True
                elif len(interactable["information"]) > 0:
                    notes.append(interactable["information"])
                    interactable["information"] = ""
                    interactable["taken"] = True
            elif len(interactable["required_information"]) > 0:
                if interactable["taken"] is False:
                    player_input = input("Provide information: ")
                    if player_input == interactable["required_information"]:
                        print(interactable["text_unlock"])
                        if len(interactable["item"]) > 0:
                            current_place["items"].append({"name": interactable["item"], "text": interactable["text_item"]})
                            interactable["item"] = ""
                            interactable["taken"] = True
                        elif len(interactable["information"]) > 0:
                            notes.append(interactable["information"])
                            interactable["information"] = ""
                            interactable["taken"] = True
            return
    print("I can't look at something that isn't there.")


def action_take(game_data, *args):
    if len(current_place["items"]) == 0:
        print("There is nothing to take here... only air... take as much as you need. :)")
        return
    if len(args) == 0:
        print("I can't take the nothing.")
        return
    
    item_to_take = args[0]

    taken = False
    items = current_place["items"]
    for item_index in range(len(items)):
        if items[item_index]["name"] == item_to_take:
            backpack.append(current_place["items"].pop(item_index)["name"])
            taken = True
            break
    if taken == False:
        print("This item does not exist here.")


def action_backpack(game_data, *args):
    if len(backpack) > 0:
        print("Your backpack contains the following items:")
        for item in backpack:
            print(f"- {item}")
    else:
        print("Your backpack is empty")
    print("")


def action_notes(game_data, *args):
    if len(notes) > 0:
        print("Your notes:")
        for note in notes:
            print(f"- {note}")
    else:
        print("You don't have any notes.")
    print("")


def action_use(game_data, *args):
    if len(args) == 0:
        print("How am I supposed to use the nothing?")
    elif len(args) == 1:
        print("What am I supposed to do with it?")
    elif len(args) == 2:
        if args[0] in backpack and args[1] not in backpack:
            # use <item> <interactable>
            interactables = list(filter(lambda interactable: interactable["name"] == args[1], current_place["interactables"] ))
            if len(interactables) == 1:
                interactable = interactables[0]
                if args[0] == interactable["required_item"]:
                    print(interactable["text_unlock"])
                    if len(interactable["item"]) > 0:
                        current_place["items"].append({"name": interactable["item"], "text": interactable["text_item"]})
                        interactable["item"] = ""
                        interactable["taken"] = True
                    elif len(interactable["information"]) > 0:
                        global notes
                        notes.append(interactable["information"])
                        interactable["information"] = ""
                        interactable["taken"] = True
                else:
                    print(f"I can't use {args[0]} with {args[1]}")
            else:
                print(f"I can't use {args[0]} with {args[1]}")
        elif args[0] in backpack and args[1] in backpack:
            # use <item1> <item2>
            combinations = game_data["combinations"]
            for combination_index in range(len(combinations)):
                combination = combinations[combination_index]
                if args[0] in combination["items"] and args[1] in combination["items"]:
                    print(combination["text"])
                    backpack.remove(args[0])
                    backpack.remove(args[1])
                    backpack.append(combination["new_item"])
                    combinations.pop(combination_index)
                    break
        else:
            print("I don't think it is a good idea.")  


def action_help(game_data, *args):
    help = """go
    go <place>
    You can go to places adjacent to your current location.

look
    look <item>
    look around
    You can examine items at current place.

take
    take <item>
    You may take items at current place.

backpack
    backpack
    You can see the content of your backpack.

use
    use <item>
    use <item1> <item2>
    use <item> <interactable>
    You may use item at current place or combine items to get something new.
    You can use item with interactables in a place. Look for hints in a place's description.

help
    help
    Get this description, but you already figured that out. ;)

exit
    exit
    exit y
    You can quit the game. Note that the game process is not saved.
"""
    print(help)


def action_exit(game_data, *args):
    global game_run
    if len(args) == 0:
        answer = input(f"Would you really like to exit? y/n\n{PROMPT}")
        if answer == "y":
            game_run = False
        elif answer == "n":
            game_run = True
    elif args[0] == "y":
        game_run = False


def action_none(*args):
    pass


ACTIONS = {
    "go": action_go,
    "look": action_look,
    "take": action_take,
    "backpack": action_backpack,
    "notes": action_notes,
    "use": action_use,
    "help": action_help,
    "exit": action_exit
}


def get_game_data(file_name):
    '''
    Opens jsnon file that holds all the game data (rooms, items, texts etc)
    
    :param file_name: Game data file name in the same folder with the source code.
    :type n: str
    :return: The loaded game data.
    :rtype: dict
    '''
    try:
        file = open(file_name, "r")
    except:
        print(f"Could not open {file_name}")
        return {}
    else:
        return json.load(file)


def get_place_by_name(place_name, game_data):
    place = list(filter(lambda place: place["name"] == place_name, game_data["places"] ))
    if len(place) == 0:
        return None
    else:
        return place[0]


def process_user_input():
    '''
    Processes user input from command line.

    :return: An action and a list of arguments based on the user input.
    :rtype: function, list
    '''
    user_input = input(PROMPT).split()
    if len(user_input) == 0:
        return action_none
    
    action = user_input[0]
    args = user_input[1:]

    if action not in ACTIONS.keys():
        return action_none, []
    else:
        return ACTIONS[action], args


def main():
    global current_place
    game_data = get_game_data(GAME_DATA)
    current_place = get_place_by_name("startplace", game_data)
    # TODO: print welcome text, CLS Adventures or something like that

    while game_run:
        if current_place["visited"] == False:
            current_place["visited"] = True
            print(f"*** {current_place['name']} ***")
            print(current_place["text"])
            print_interactables()
            print("")
            print_items_around()
            print("")
            print_places_around()
            print("")
        
        # TODO: Get random text for this question and for others too
        print("What shall be your next move?")
        action, args = process_user_input()
        action(game_data, *args)

        print("")

if __name__ == "__main__":
    main()