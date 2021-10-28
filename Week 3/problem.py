class Node:
    def __init__(self, state, cost, move = "", parent= None) :
        self.parent = parent
        self.state = state
        self.move = move
        self.cost = cost

class Problem:
    def __init__(self, size, initial_state, goal):
        self.initial_state = initial_state
        self.goal = goal
        self.size = size
    
    
    # Diz se o estado atual chegou ao objetivo.
    def objective_test(self, state):
        return state == self.goal

    # Pega a coordenada x a partir de um index do vetor
    def get_x(self, index):
        return index - self.get_y(index) * self.size

    # Pega a coordenada y a partir de um index do vetor
    def get_y(self, index):
        return index // self.size

    
    
    # Pega aa coordenadas x e y a partir de um index do vetor
    def get_coords(self, index):
        return self.get_x(index), self.get_y(index)

    
    # Pega o index do vetor a partir das coordenadas x e y
    def get_index(self, x, y):
        return y * self.size + x

    
    # Pega as possíveis ações que o problema pode ter
    def actions(self, state):
        moves = ["Up", "Right", "Left", "Down"]
        index = state.index(0)
        x, y = self.get_coords(index)

        if x == 0:
            moves.remove("Left")
        elif x == self.size - 1:
            moves.remove("Right")

        if y == 0:
            moves.remove("Up")
        elif y == self.size - 1:
            moves.remove("Down")

        return moves

    
    # Faz o movimento 'action' no estado 'estate' e retorna o novo estado
    def move(self, state, action):
        result = state.copy()
        index = state.index(0)
        x, y = self.get_coords(index)

        if action == "Up":
            y -= 1
        elif action == "Down":
            y += 1
        elif action == "Left":
            x -= 1
        elif action == "Right":
            x += 1

        new_index = self.get_index(x, y)

        result[index], result[new_index] = result[new_index], result[index]

        return result

    
    # Pega o path que fez chegar no 'node'
    def get_path(self, node):
        moves = []

        while node.parent:
            moves.append(f"'{node.move}'")
            node = node.parent

        moves.reverse()
        return ", ".join(moves)