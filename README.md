# D100 Table Roller

A simple desktop app for rolling on random tables during tabletop RPG sessions.

## Features

- Browse and organize tables by category
- Three rolling modes: random, specific number, or multiple rolls
- Automatic dice notation processing (1d6, 2d8, etc.)
- Search tables by name
- Clean, minimal interface

## Setup

Just run the Python script:

```
python d100_roller_python.py
```

Requires Python 3.6+ with tkinter (usually included).

## Using Tables

The app looks for `.txt` files in a `tables` folder. If none exist, it creates some sample tables to get you started.

### Table Format

Each table is a simple text file with one entry per line:

```
Rusty Dagger
Iron Sword
Silver Blade
Enchanted Bow (+1d4 damage)
```

### Organizing Tables

Put tables in subfolders to organize by category:

```
tables/
  items/
    weapons.txt
    armor.txt
  encounters/
    forest.txt
    dungeon.txt
```

## Rolling

1. Pick a table from the browser
2. Choose your rolling mode:
   - **Random**: Single random roll
   - **Specific**: Enter exact number (1-100)
   - **Multiple**: Roll multiple times
3. Click Roll

The app automatically processes dice notation like "1d6" or "2d8" and shows the actual roll result.

## Managing Tables

- **Open Folder**: Opens the tables directory in your file manager
- **Add Table**: Import a new table file
- **Search**: Filter tables by name

That's it. Simple tool for simple needs.