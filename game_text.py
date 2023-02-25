from random import randint

def get_random_text(text_list):
    return text_list[randint(0, len(text_list) - 1)]


action_go_no_args = "And how am I supposed to go nowhere?"


action_go_current_place = "You are exactly there."


action_go_not_adjacent = "I'm afraid this place is not around here."


action_look_no_args = [
    "I can look at nothing... only if I'm meditating.",
    "What should I look at?"
]


action_look_unkown_object = [
    "I can't look at something that isn't there.",
    "I wish I could see that!"
]


action_take_no_args = [
    "I can't take the nothing.",
    "Give me an object to take!"
]


action_take_no_items = [
    "There is nothing here to take... only air... take as much as you need. :)",
    "Good try, but there is nothing here."
]


action_take_no_match = [
    "I'm afraid that is not possible.",
    "There is no such an item in this place.",
    "I just can't find this item here, try to take something else."
]


action_backpack = "Your backpack contains the following items:"


action_notes = "Your notes:"


action_notes_empty = "You don't have any notes."


action_backpack_empty = "Your backpack is empty."


action_use_no_args = "How am I supposed to use the nothing?"


action_use_one_arg = "What am I supposed to do with it?"


action_use_cannot = "I can't use {arg0} with {arg1}"


action_use_no_items = "I don't think it is a good idea."


action_help = """go
    go <place>
    You can go to places adjacent to your current location.

look
    look around
    look <item>
    look <interactable>
    You can examine items or interactables at current place.

take
    take <item>
    You can take items at current place.

backpack
    backpack
    You can see the content of your backpack.

notes
    notes
    You can see the content of you notes.    

use
    use <item>
    use <item1> <item2>
    use <item> <interactable>
    You can use item at current place or combine items to get something new.
    You can use item with an interactables. Look for hints in a place's description.

help
    help
    Get this description, but you already figured that out. ;)

exit
    exit
    exit y
    You can quit the game. Note that the game process is not saved.
"""


