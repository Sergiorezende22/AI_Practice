from problem import Problem

def manhattan_distance(problem:Problem, initial_state, final_state):
    result = 0
    x = y = x_s = y_s = 0
    for index, item in enumerate(initial_state):
        x, y = problem.get_coords(index)
        for index_s, item_s in enumerate(final_state):
            if item_s == item:
                x_s, y_s = problem.get_coords(index_s)
                break
        result += abs(x - x_s) + abs(y - y_s)
        
    return result