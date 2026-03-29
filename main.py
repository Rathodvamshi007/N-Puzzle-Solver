from environment import Env
from solver import AStarSolver, BFSSolver, DFSSolver
from heuristic import get_manhattan_distance, get_linear_conflict
import time

def flatten(state):
    return [num for row in state for num in row]

def print_path(path):
    for i, step in enumerate(path):
        print(f"Step {i}:")
        for j in range(0, len(step), 3):
          print(list(step[j:j+3]))
        print()

def main():
    n = int(input("Size: "))
    initial = [list(map(int, input().split())) for _ in range(n)]

    puzzle = Env(initial)

    print("1.A* 2.BFS 3.DFS")
    choice = int(input("Choice: "))
