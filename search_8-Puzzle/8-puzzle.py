import sys
import time

import resource

from search import *
from problem import *
from heuristics import manhattan_distance

def main():
    method = sys.argv[1]
    initial_state = [int(i) for i in sys.argv[2].split(',')]
    if method == 'idfs':
        minimum = int(sys.argv[3])
        maximum = int(sys.argv[4])
        step = int(sys.argv[5])

    problem = Problem(3, initial_state, [0, 1, 2, 3, 4, 5, 6, 7, 8])
    
    start_time = time.time()
    if method == 'bfs':
        result = bfs(problem)
    elif method == 'dfs':
        result = dfs(problem)
    elif method == 'idfs':
        result = idfs(problem, minimum, maximum, step)
    elif method == 'astar':
        result = astar(problem, manhattan_distance)
    elif method == 'greedy':
        result = greedy(problem, manhattan_distance)
    final_time = time.time()

    node = result['node']
    file = open("ans/" + method + ".txt", "w")

    if method == 'idfs':
        file.write(f"min_limit: {minimum}\n")
        file.write(f"max_limit: {maximum}\n")
        file.write(f"step: {step}\n")
    if node:
        file.write(f"path_to_goal: [{problem.get_path(node)}]\n")
        file.write(f"cost_of_path: {node.cost}\n")
    else:
        file.write(f"path_to_goal: Path was not found\n")
    file.write(f"nodes_expanded: {result['scanned']}\n")
    file.write(f"fringe_size: {result['finalfrontier']}\n")
    file.write(f"max_fringe_size: {result['maxfrontier']}\n")
    if node:
        file.write(f"search_depth: {node.cost}\n")
    file.write(f"max_search_depth: {result['maxdepth']}\n")
    file.write(f"running_time: {final_time - start_time} s\n")
    file.write(f"max_ram_usage: {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000.0} kb\n")


main()