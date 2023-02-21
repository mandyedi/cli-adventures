from sys import argv
import json
from types import SimpleNamespace
import game_text as gt
from pyfiglet import Figlet

game_run = True
backpack = []
notes = []
current_place = {}

PROMPT = ">:"
GAME_DATA = "data_beta.json"

def print_interactables():
    for interactable in current_place.interactables:
        if interactable.taken is True:
            print(interactable.text_place_taken)
        else:
            print(interactable.text_place)

def print_items_around():
    global current_place
    if len(current_place.items) > 0:
        print("Collectible items around here:")
        for item in current_place.items:
            print(f"- {item.name}")
    else:
        print("There isn't anything here to take. :(")


def print_places_around():
    global current_place
    if len(current_place.adjacent_places) > 0:
        print("Places to go from here:")
        for place in current_place.adjacent_places:
            print(f"- {place.name}")
    else:
        print("You are trapped. There is no scape from here. :(")

def action_go(game_data, *args):
    global current_place
    if len(args) == 0:
        print(gt.action_go_no_args)
    else:
        if args[0] == current_place.name:
            print(gt.action_go_current_place)
            return

        adjacent_places = [place.name for place in current_place.adjacent_places]
        if args[0] not in adjacent_places:
            print(gt.action_go_not_adjacent)
            return

        place = get_place_by_name(args[0], game_data)
        current_place.visited = False
        current_place = place


def action_look(game_data, *args):
    if len(args) == 0:
        print(gt.get_random_text(gt.action_look_no_args))
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
    for item in current_place.items:
        if item.name == subject_to_look:
            print(item.text)
            return
    
    # Handle interactable
    global notes
    for interactable in current_place.interactables:
        if interactable.name == subject_to_look:
            if interactable.taken is True:
                print(interactable.text_look_taken)
            else:
                print(interactable.text_look)

            if len(interactable.required_item) == 0 and len(interactable.required_information) == 0:
                if len(interactable.item) > 0:
                    item = SimpleNamespace(name=interactable.item, text=interactable.text_item)
                    current_place.items.append(item)
                    interactable.item = ""
                    interactable.taken = True
                elif len(interactable.information) > 0:
                    notes.append(interactable.information)
                    interactable.information = ""
                    interactable.taken = True
            elif len(interactable.required_information) > 0:
                if interactable.taken is False:
                    player_input = input("Provide information: ")
                    if player_input == interactable.required_information:
                        print(interactable.text_unlock)
                        if len(interactable.item) > 0:
                            item = SimpleNamespace(name=interactable.item, text=interactable.text_item)
                            current_place.items.append(item)
                            interactable.item = ""
                            interactable.taken = True
                        elif len(interactable.information) > 0:
                            notes.append(interactable.information)
                            interactable.information = ""
                            interactable.taken = True
            return
    print(gt.get_random_text(gt.action_look_unkown_object))


def action_take(game_data, *args):
    if len(args) == 0:
        print(gt.get_random_text(gt.action_take_no_args))
        return
    elif len(current_place.items) == 0:
        print(gt.get_random_text(gt.action_take_no_items))
        return
    
    item_to_take = args[0]

    taken = False
    items = current_place.items
    for item_index in range(len(items)):
        if items[item_index].name == item_to_take:
            backpack.append(current_place.items.pop(item_index).name)
            taken = True
            break
    if taken == False:
        print(gt.get_random_text(gt.action_take_no_match))


def action_backpack(game_data, *args):
    if len(backpack) > 0:
        print(gt.action_backpack)
        for item in backpack:
            print(f"- {item}")
    else:
        print(gt.action_backpack_empty)


def action_notes(game_data, *args):
    if len(notes) > 0:
        print(gt.action_notes)
        for note in notes:
            print(f"- {note}")
    else:
        print(gt.action_notes_empty)


def action_use(game_data, *args):
    if len(args) == 0:
        print(gt.action_use_no_args)
    elif len(args) == 1:
        print(gt.action_use_one_arg)
    elif len(args) == 2:
        if args[0] in backpack and args[1] not in backpack:
            # use <item> <interactable>
            interactables = list(filter(lambda interactable: interactable.name == args[1], current_place.interactables ))
            if len(interactables) == 1:
                interactable = interactables[0]
                if args[0] == interactable.required_item:
                    print(interactable.text_unlock)
                    if len(interactable.item) > 0:
                        item = SimpleNamespace(name=interactable.item, text=interactable.text_item)
                        current_place.items.append(item)
                        interactable.item = ""
                        interactable.taken = True
                    elif len(interactable.information) > 0:
                        global notes
                        notes.append(interactable.information)
                        interactable.information = ""
                        interactable.taken = True
                else:
                    print(gt.action_use_cannot.format(arg0=args[0], arg1=args[1]))
            else:
                print(gt.action_use_cannot.format(arg0=args[0], arg1=args[1]))
        elif args[0] in backpack and args[1] in backpack:
            # use <item1> <item2>
            combinations = game_data.combinations
            for combination_index in range(len(combinations)):
                combination = combinations[combination_index]
                if args[0] in combination.items and args[1] in combination.items:
                    print(combination.text)
                    backpack.remove(args[0])
                    backpack.remove(args[1])
                    backpack.append(combination.new_item)
                    combinations.pop(combination_index)
                    break
        else:
            print(gt.action_use_no_items)  


def action_help(game_data, *args):
    print(gt.action_help)


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
        return json.load(file, object_hook=lambda d: SimpleNamespace(**d))


def get_place_by_name(place_name, game_data):
    place = list(filter(lambda place: place.name == place_name, game_data.places ))
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

    data_file = GAME_DATA
    if len(argv) == 2:
        data_file = argv[1]
    game_data = get_game_data(data_file)
    
    current_place = get_place_by_name("startplace", game_data)

    f = Figlet(font="big")
    print(f.renderText("CLI Adventures"))

    while game_run:
        if current_place.visited == False:
            current_place.visited = True
            print(f"*** {current_place.name} ***")
            print(current_place.text)
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