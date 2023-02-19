# Documentation
## Actions
### go
```
go <place>
```


### look
```
look around
look <item>
look <interactable>
```

### take
```
take <intem>
```

### backpack
```
backpack
```

### use
```
use <item1> <item2>
use <item> <interactable>
```

### help
```
help
```

### exit
```
exit
exit y
```

## Interactables
```
name:
    The name that is shown to the user.
    Also an id the identifiy.
item:
    Contained by the interactable object.
    If has requirement:
        Use the correct item with interactable.
        Item is moved to place's items.
        From place's item it can be taken.
    If has no requirement:
        Item can be taken.
information:
    Contained by the interactable object.
    If has requirement:
        Use interactable. (give hint in text_look that it can be used)
        Information is moved to player's notes.
    If has no requirement:
        Information is moved to player's notes.
required_item:
    Use item with interactable.
required_information:
    Use interactable and answer the correct information from player's notes.
text_place:
    Printed when player enters a place or look around at a place.
text_item:
    Moved with item to place's item.
text_look:
    Printed when player look interactable.
    Informs user if it has a requirement.
    May print hint about requirements.
text_look_taken:
    If item taken or information is moved to user's notes the interactable still can be looked.
text_unlock:
    Print when the required item is used.
    Print when the correct information is given.
    Also can be used when there is no requirement and player takes it.
```

- Name is unique on global scope.  
- Interactable can contain item or information but not both at the same time.
  - IDEA: contain both and also array of items and array of informations.  

### Interactable Flow
**Has Item No Requirements**  
1. text_place is printed when entering a place
2. player looks interactable:
   - text_look is printed
   - item is moved to place's items along with text_item
   - item is removed from requirement's items
   - text_look is removed, indicateing that item is no more there 
3. player looks again interactable: text_look_taken is printed (if text_look is empty)
4. player takes item from place's items

**Has Information No Requirements**  
1. text_place is printed when entering a place
2. player looks interactable:
   - text_look is printed
   - information is moved to players's notes
   - information is removed from requirement's items
   - text_look is removed, indicateing that information is no more there
3. player looks again interactable: text_look_taken is printed (if text_look is empty)

**Has Item Has Requirements**  
1. text_place is printed when entering a place
2. player looks interactable:
   - text_look is printed
3. player uses item with requirements
   - text_unlock is printed
   - item is moved to place's items along with text_item
   - item is removed from requirement's items
   - text_look is removed, indicating that item is no more there 
4. player looks again interactable: text_look_taken is printed (if text_look is empty)
5. player takes item from place's items

**Has Information Has Requirements**  
1. text_place is printed when entering a place
2. player looks interactable:
   - text_look is printed
   - input is given to user, asks for required information
3. player gives required information
   - text_unlock is printed
   - information is moved to players's notes
   - information is removed from requirement's items
   - text_look is removed, indicateing that information is no more there
4. player looks again interactable: text_look_taken is printed (if text_look is empty)