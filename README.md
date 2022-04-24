# Pygame-Tetris
## Description
An attempt to improve pygame library understanding by implementing Tetris 

## Table of contents
- [Pygame basics](#[pygame-basics])
- [Tetris](#tetris)
- [Convert to Executable](#convert-to-executable)
- [References](#references)

## Pygame Basics

*pygame-basics.py* contains a basic implementation of jet-bird dodge game. It introduces basic ideas about surface, rect, game loop, sprites, custom events, collision detection and time

## Tetris

Implementation for basic tetris game taken from [InventWithPython](https://inventwithpython.com/pygame/chapter7.html). Additional features added - 
- next queue
- color scheme modes
- Resizable, scalable display

## Convert to executable

- install pyinstaller
- run following command in terminal to convert *filename.py* to executable

```
pyinstaller filename.py --onefile -noconsole
```
- A *build* directory, *dist* directory and *filename.spec* file will be created in current working directory
- Game executable ( *filename.exe* ) can be found in *dist* directory
- All assets should be moved to dist folder manually 

## References
- Pygame Basics
    - [RealPython](https://realpython.com/pygame-a-primer/)
    - [Invent With Python](https://inventwithpython.com/pygame/)
- Tetris
- Py to exe
    - [Making an Executable from a Pygame Game (PyInstaller)](https://youtu.be/lTxaran0Cig)


