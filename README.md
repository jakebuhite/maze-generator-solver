# Maze Generator and Solver
Maze Generator and Solver made with Python

## Dependencies
+ memory-profiler 0.61.0
+ psutil          5.9.5

## Installation
+ Ensure dependencies are installed
+ Download and extract the source code
+ In the source code folder, run `python main.py` or `python3 main.py`

## Usage
Maze Generator and Solver can be used for generating mazes and collecting data. 

### Maze Generation
The maze generator offers the ability to generate text files with or without the solution. To generate the maze without the solution, ensure that the following is set in `main.py`:
```
maze.printMaze()
```
To generate the maze with the solution, ensure that the following is set in `main.py`:
```
maze.printMaze(true)
```

### Collecting Data
To collect data, ensure that `dataCollection()` is uncommented in `main.py` and `main()` is commented (and the opposite for generating mazes). This program utilizes *memory-profiler* to gather the peak memory usage during maze generation and solving. *timeit* is used to determine the time each algorithm takes to execute. The metrics gathered when running this program can be modified in `metrics.py`.
