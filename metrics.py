# Imports
import csv
from maze import Maze
from datetime import datetime
from timeit import default_timer as timer
from memory_profiler import memory_usage

def dataCollection():
    """
    Collects runtime of maze generator and solver (individually), peak memory usage, and path length (A*)

    :return: None
    """
    filename = "elapsed-" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"
    outputCSV = open("data\\" + filename, "a", newline="")
    writer = csv.writer(outputCSV, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Dimensions", "Runtime of Generator (s)", "Runtime of Solver (s)", "Peak Memory Usage During Maze Generation (MiB)", "Peak Memory Usage During Maze Solving (MiB)"])

    for i in range(5, 100, 5):
        maze = Maze(i, i)

        # Get time before and after generation
        start = timer()
        generateMemUsage = max(memory_usage(maze.generateMaze))
        elapsedGen = timer() - start # seconds

        # Get time before and after solving
        start = timer()
        solvedMemUsage = max(memory_usage(maze.solveMaze))
        elapsedSolve = timer() - start # seconds

        writer.writerow(["{}x{}".format(i, i), elapsedGen, elapsedSolve, generateMemUsage, solvedMemUsage])
        print("UPDATE > " + "{}x{}".format(i, i) + " " + str(elapsedGen) + " " + str(elapsedSolve) + " " + str(generateMemUsage) + " " + str(solvedMemUsage))
        
        # Delete maze
        del maze
    
    for i in range(100, 1000, 50):
        maze = Maze(i, i)

        # Get time before and after generation
        start = timer()
        generateMemUsage = max(memory_usage(maze.generateMaze))
        elapsedGen = timer() - start # seconds

        # Get time before and after solving
        start = timer()
        solvedMemUsage = max(memory_usage(maze.solveMaze))
        elapsedSolve = timer() - start # seconds

        writer.writerow(["{}x{}".format(i, i), elapsedGen, elapsedSolve, generateMemUsage, solvedMemUsage])
        print("UPDATE > " + "{}x{}".format(i, i) + " " + str(elapsedGen) + " " + str(elapsedSolve) + " " + str(generateMemUsage) + " " + str(solvedMemUsage))
        
        # Delete maze
        del maze

    for i in range(1000, 8001, 500):
        maze = Maze(i, i)

        # Get time before and after generation
        start = timer()
        generateMemUsage = max(memory_usage(maze.generateMaze))
        elapsedGen = timer() - start # seconds

        # Get time before and after solving
        start = timer()
        solvedMemUsage = max(memory_usage(maze.solveMaze))
        elapsedSolve = timer() - start # seconds

        writer.writerow(["{}x{}".format(i, i), elapsedGen, elapsedSolve, generateMemUsage, solvedMemUsage])
        print("UPDATE > " + "{}x{}".format(i, i) + " " + str(elapsedGen) + " " + str(elapsedSolve) + " " + str(generateMemUsage) + " " + str(solvedMemUsage))
        
        # Delete maze
        del maze

    outputCSV.close()
