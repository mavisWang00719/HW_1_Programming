## Introduction

Download or clone this repository. This code, and the idea for the project, comes from [UC Berkeley](https://inst.eecs.berkeley.edu//~cs188/pacman/home.html).

* Open up the Windows Command Line or Mac Terminal or Linux Terminal.

* Change your directory to the folder with the pacman code. You should see a file called `commands.txt` and three folders: `py`, `layouts` and `test_cases` .

* Run some of these commands (as listed in `commands.txt`) to make sure your setup works. Below are some examples:

```
python3 py/pacman.py
```

```
python3 py/pacman.py --layout tinyMaze --pacman GoWestAgent
```

* Make sure you can execute pacman. See what happens when you run the following command:

```
python3 py/pacman.py --layout tinyMaze --pacman GoWestAgent
```

* running the following command so that depth-first search works: 
```
python3 py/pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
```

* running the following command so that breadth-first search works: 
```
python3 py/pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```
* running the following command so that uniform Cost Search works: 
```
python3 py/pacman.py -l mediumMaze -p SearchAgent -a fn=ucs 
```
* running the following command so that A Star Search works: 
```
python3 py/pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

```

### Implementation
* We note that, the provided commands are designed to work with Mac/Linux with Python version 3. If your are using Windows (like me!), you can use the COMMAND LINE (CMD), and make the following changes: (1) Please use \ instead of / while specifying the path to the file. (2) If it still does not work, you may try replacing "python3" with "py -3" in the command you're executing on CMD. Example command that works for us: "py -3 py\autograder.py"

####  Files you'll edit and submit :
* `py/search.py`: Where your search algorithms will reside.

#### Files you'll want to take a look at:
* `py/searchAgents.py`: Where all search-based agents are defined.
* `py/util.py`: Useful data structures you'll need for defining search algorithms.

#### Supporting files you can ignore (unless you're curious):

* `py/pacman.py`: The main file that runs Pacman games. This file describes a `Pacman` `GameState` type, which you use in this project.
* `py/game.py`: The logic behind how the Pacman world works. This file describes several supporting types like `AgentState`, `Agent`, `Direction`, and `Grid`.
* `py/graphicsDisplay.py`: Graphics for Pacman
* `py/graphicsUtils.py`: Support for Pacman graphics
* `py/textDisplay.py`: ASCII graphics for Pacman
* `py/ghostAgents.py`: Agents to control Ghosts
* `py/keyboardAgents.py`: Keyboard interfaces to control Pacman
* `py/layout.py`: Code for reading layout files and storing their contents
* `py/autograder.py`: Project autograder
* `py/testParser.py`: Parses autograder test and solution files
* `py/testClasses.py`: General autograding test classes
* `py/test_cases/`: Directory containing the test cases for each question
* `py/searchTestClasses.py`: Testcases to support autograding



