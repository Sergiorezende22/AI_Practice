from collections import deque
from problem import Problem, Node
from heapq import heapify, heappush, heappop

def bfs(problem:Problem):
    maxdepth = 0
    maxfrontier = 0
    # Criando o primeiro nó
    node = Node(problem.initial_state, 0, 0)
    
    if problem.objective_test(node.state):
        return {"node": node, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": 0, "scanned": 0}
    
    # Criando as listas que vão ser usadas
    edge = deque()
    edge.append(node)
    explored = set()
    
    # Enquanto edge não for vazia
    while edge:
        # Pega o primeiro valor que entrou na fila e adiciona nos explorados
        node = edge.popleft()
        explored.add(str(node.state))
        
        # Pega as possíveis ações que podemos fazer a partir do estado atual
        for action in problem.actions(node.state):
            
            # Realiza a ação e pega o novo estado
            newstate = problem.move(node.state, action)
            
            # Cria o filho do nó atual com a ação selecionada
            son = Node(newstate, node.cost + 1, node.depth + 1, action, node)
            
            # Checa se o filho já foi explorado
            if str(son.state) not in explored:
                # Gravando a variável de maior profundidade
                if son.depth > maxdepth:
                    maxdepth = son.depth
                    
                # Se o filho for a resposta, retorna a solução
                if problem.objective_test(son.state):
                    return {"node": son, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": len(edge), "scanned": len(explored)}
                
                # Adiciona o filho a fila e na lista de explorados
                edge.append(son)
                explored.add(str(son.state))


        # Gravando a variável de maior fronteira
        if len(edge) > maxfrontier: 
            maxfrontier = len(edge)
        
        
    return {"node": None, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": len(edge), "scanned": len(explored)}


def dfs(problem:Problem):
    maxdepth = 0
    maxfrontier = 0
    # Criando o primeiro nó
    node = Node(problem.initial_state, 0, 0)

    if problem.objective_test(node.state):
        return {"node": node, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": 0, "scanned": 0}

    # Criando as listas que vão ser usadas
    edge = deque()
    edge.append(node)
    explored = set()
    
    # Enquanto edge não for vazia
    while edge:
        # Pega o último valor que entrou na fila e adiciona nos explorados
        node = edge.pop()
        explored.add(str(node.state))

        # Pega as possíveis ações que podemos fazer a partir do estado atual
        for action in problem.actions(node.state):
            
            # Realiza a ação e pega o novo estado
            newstate = problem.move(node.state, action)

            # Cria o filho do nó atual com a ação selecionada
            son = Node(newstate, node.cost + 1, node.depth + 1, action, node)
            
            # Checa se o filho já foi explorado
            if str(son.state) not in explored:
                # Gravando a variável de maior profundidade
                if son.depth > maxdepth:
                    maxdepth = son.depth

                # Se o filho for a resposta, retorna a solução
                if problem.objective_test(son.state):
                    return {"node": son, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": len(edge), "scanned": len(explored)}

                # Adiciona o filho a fila e na lista de explorados
                edge.append(son)
                explored.add(str(son.state))

        # Gravando a variável de maior fronteira
        if len(edge) > maxfrontier: 
            maxfrontier = len(edge)
        
        
    return {"node": None, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": len(edge), "scanned": len(explored)}


def idfs(problem:Problem, minimum, maximum, step):
    
    # Criação da iteração entre minimo e maximo com o step
    for limit in range(minimum, maximum, step):

        maxdepth = 0
        maxfrontier = 0
        # Criando o primeiro nó
        node = Node(problem.initial_state, 0,0)

        if problem.objective_test(node.state):
            return {"node": node, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": 0, "scanned": 0}

        # Criando as listas que vão ser usadas
        edge = deque()
        edge.append(node)
        explored = set()
        
        # Enquanto edge não for vazia
        while edge:
            # Pega o último valor que entrou na fila e adiciona nos explorados
            node = edge.pop()
            explored.add(str(node.state))
            
            # Checar se o custo passou do limite e caso passe pegar o próximo limite
            if node.cost > limit:
                break
        
            # Pega as possíveis ações que podemos fazer a partir do estado atual
            for action in problem.actions(node.state):

                # Realiza a ação e pega o novo estado
                newstate = problem.move(node.state, action)

                # Cria o filho do nó atual com a ação selecionada
                son = Node(newstate, node.cost + 1, node.depth + 1, action, node)
                
                # Checa se o filho já foi explorado
                if str(son.state) not in explored:
                    # Gravando a variável de maior profundidade
                    if son.depth > maxdepth:
                        maxdepth = son.depth

                    # Se o filho for a resposta, retorna a solução
                    if problem.objective_test(son.state):
                        return {"node": son, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": len(edge), "scanned": len(explored)}

                    # Adiciona o filho a fila e na lista de explorados
                    edge.append(son)
                    explored.add(str(son.state))


            # Gravando a variável de maior fronteira
            if len(edge) > maxfrontier: 
                maxfrontier = len(edge)
        
        
    return {"node": None, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": len(edge), "scanned": len(explored)}


def astar(problem:Problem, heuristic):
    maxdepth = 0
    maxfrontier = 0
    # Criando o primeiro nó
    node = Node(problem.initial_state, heuristic(problem, problem.goal, problem.initial_state), 0)
    
    if problem.objective_test(node.state):
        return {"node": node, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": 0, "scanned": 0}
    
    # Criando as listas que vão ser usadas
    edge = []
    # Criando um heap para usar como lista ordenada
    heapify(edge)
    heappush(edge, node)
    explored = set()
    i = 0
    # Enquanto edge não for vazia
    while edge:
        # Pega o menor valor da heap
        node = heappop(edge)
        explored.add(str(node.state))

        # Pega as possívels ações que podems fazer
        for action in problem.actions(node.state):
            # Realiza a ação e pega o novo estado
            newstate = problem.move(node.state, action)
            
            # Cria o filho do nó atual com a ação selecionada
            son = Node(newstate, node.depth + 1 + heuristic(problem, problem.goal, newstate), node.depth + 1, action, node)
            
            # Checa se o filho já foi explorado
            if str(son.state) not in explored:
                # Gravando a variável de maior profundidade
                if son.depth > maxdepth:
                    maxdepth = son.depth

                # Se o filho for a resposta, retorna a solução
                if problem.objective_test(son.state):
                    return {"node": son, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": len(edge), "scanned": len(explored)}
                
                # Adiciona o filho a fila e na lista de explorados
                heappush(edge, son)
                explored.add(str(son.state))

        # Gravando a variável de maior fronteira
        if len(edge) > maxfrontier: 
            maxfrontier = len(edge)
        
        
    return {"node": None, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": len(edge), "scanned": len(explored)}


def greedy(problem:Problem, heuristic):
    maxdepth = 0
    maxfrontier = 0
    # Criando o primeiro nó
    node = Node(problem.initial_state, heuristic(problem, problem.goal, problem.initial_state), 0)
    
    if problem.objective_test(node.state):
        return {"node": node, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": 0, "scanned": 0}
    
    # Criando as listas que vão ser usadas
    edge = deque()
    edge.append(node)
    explored = set()
    
    # Enquanto edge não for vazia
    while edge:
        # Pega o valor que entrou na fila e adiciona nos explorados
        node = edge.popleft()
        explored.add(str(node.state))
        
        # Pega as possívels ações que podemos fazer e ordena de acordo com o custo calculado pela heuristica
        actions = sorted(problem.actions(node.state), key = lambda action: heuristic(problem, problem.goal, problem.move(node.state, action)))

        for action in actions:
            
            # Realiza a ação e pega o novo estado
            newstate = problem.move(node.state, action)
            
            # Cria o filho do nó atual com a ação selecionada
            son = Node(newstate, heuristic(problem, problem.goal, newstate), node.depth + 1, action, node)
            
            # Checa se o filho já foi explorado
            if str(son.state) not in explored:
                # Gravando a variável de maior profundidade
                if son.depth > maxdepth:
                    maxdepth = son.depth

                # Se o filho for a resposta, retorna a solução
                if problem.objective_test(son.state):
                    return {"node": son, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": len(edge), "scanned": len(explored)}
                
                # Adiciona o filho a fila e na lista de explorados
                edge.append(son)
                explored.add(str(son.state))
                # Achamos o filho com o menor custo que ainda não foi explorado, então vamos para o próximo
                break

        # Gravando a variável de maior fronteira
        if len(edge) > maxfrontier: 
            maxfrontier = len(edge)
        
        
    return {"node": None, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": len(edge), "scanned": len(explored)}