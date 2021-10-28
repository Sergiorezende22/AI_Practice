import sys
import time

import resource

from search import *
from problem import *

def main():
    method = sys.argv[1]
    initial_state = [int(i) for i in sys.argv[2].split(',')]
    if method == 'idfs':
        minimum = int(sys.argv[3])
        maximum = int(sys.argv[4])
        step = int(sys.argv[5])

    problem = Problem(3, initial_state, [0, 1, 2, 3, 4, 5, 6, 7, 8])

    if method == 'bfs':
        start_time = time.time()
        result = bfs(problem)
        final_time = time.time()
    elif method == 'dfs':
        start_time = time.time()
        result = dfs(problem)
        final_time = time.time()
    elif method == 'idfs':
        start_time = time.time()
        result = idfs(problem, minimum, maximum, step)
        final_time = time.time()

    node = result['node']
    file = open("ans/" + method + ".txt", "w")

    if method == 'idfs':
        file.write(f"min_limit: {minimum}\n")
        file.write(f"max_limit: {maximum}\n")
        file.write(f"step: {step}\n")
    file.write(f"path_to_goal: [{problem.get_path(node)}]\n")
    file.write(f"cost_of_path: {node.cost}\n")
    file.write(f"nodes_expanded: {result['scanned']}\n")
    file.write(f"fringe_size: {result['finalfrontier']}\n")
    file.write(f"max_fringe_size: {result['maxfrontier']}\n")
    file.write(f"search_depth: {node.cost}\n")
    file.write(f"max_search_depth: {result['maxdepth']}\n")
    file.write(f"running_time: {final_time - start_time} s\n")
    file.write(f"max_ram_usage: {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000.0} kb\n")


main()