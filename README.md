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

## Ideas:
- Use pyscript to run the game on the web
  - https://github.com/pyscript/pyscript
  - https://stackoverflow.com/a/72093922
  - actions return string
  - separate game.py and engine.py
    engine only returns strings
  - engine is used from game.py and game.html too
  - fix pyfiglet issue: not supported by pyscript
- do I need global current_place?
  do I need to pass game_data to actions? isn't current_place enough?
  OR
  ```
  game_context = {
      "game_data": game_data,
      "current_place": current_place (or key of current place)
  }
  ```
- random start point from multiple startplaces
  have a different list in game data for them
- make backpack and notes part of game_data
- save game
- collect text from favorite games

## Favorite Texts
### Commandos
I'm afraid that is not possible!  
### Morrowind
Welcome Outlander!  
### Star Craft
### Monkey Island


## References
Salad Fingers: rusty spoon, Hubert Cumberdale, Marjory Stewart-Baxter, and Jeremy Fisher
The Dark Tower: riddles