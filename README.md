# CLI Invaders
#### Video Demo:  <URL HERE>
#### Description:

## TO DO
- [ ] Create a short video (that’s no more than 3 minutes in length)
      https://www.howtogeek.com/205742/how-to-record-your-windows-mac-linux-android-or-ios-screen/  
- [ ] Video includes: project’s title, your name, your city and country, and any other details that you’d like to convey to viewer
- [ ] Upload your video to YouTube
- [ ] Submit form
      https://cs50.harvard.edu/python/2022/project/  
- [ ] README.md
      - [ ] should be minimally multiple paragraphs in length
      - [ ] explain what your project is
      - [ ] what each of the files you wrote for the project contains and does
- [ ] Execute submit50 command

## Rules:
### Items
- Item: can be taken. After that it is in backpack.
- Two items: can be combined.
  - Player gets a new item.
  - The two original items are removed.
- Item: can be used at specific places:
  - New item becomes available at current place (key, tool, etc).
  - Item interacts with the surroundings (door opens, box opens).
  - Get new info (password for door, box etc).
### Interactables (objects)
- Can be opened with item: gives new item, still need to be taken
- Can provide information: password, usefull information. Added to notes right away.
### Look
- Look objects mentioned in welcome text: objects are added to place's items.
- Look item: gives detailed description.
- Look adjacent places: general descrioption or clue if entrance is locked.
  

## Ideas:
- Use package to print fancy ASCII art logo
- Instead of using text_look_taken just remov the text_place so there is nothing to interact with anymore.
- How to phrase: I do xy. You do xz.
- move texts to a different file (help, random texts, etc.)
- notes: important info noted, password, data for riddles etc.
- random start point from multiple startplaces
  have a different list in game data for them
- save game
- multiple text and choose randomly
  e.g. player wants to go to a non-existent place: (What?) (I'm afraid that is not possible!)
- use text from favorite games
  Welcome Outlander!
  I'm afraid that is not possible!
  etc.

https://stackoverflow.com/a/15882054  
```python
import json
from types import SimpleNamespace

data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
print(x.name, x.hometown.name, x.hometown.id)
```

## Favorite Texts
### Commandos
I'm afraid that is not possible!  
### Morrowind
Welcome Outlander!  

## References
Salad Fingers: rusty spoon, Hubert Cumberdale, Marjory Stewart-Baxter, and Jeremy Fisher