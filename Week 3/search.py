from collections import deque
from problem import Problem, Node

def bfs(problem:Problem):
    maxdepth = 0
    maxfrontier = 0
    # Criando o primeiro nó
    node = Node(problem.initial_state, 0)
    
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
            son = Node(newstate, node.cost + 1, action, node)
            
            # Checa se o filho já foi explorado
            if str(son.state) not in explored:
                # Se o filho for a resposta, retorna a solução
                if problem.objective_test(son.state):
                    return {"node": son, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": len(edge), "scanned": len(explored)}
                
                # Adiciona o filho a fila e na lista de explorados
                edge.append(son)
                explored.add(str(son.state))
                
                # Gravando a variável de maior profundidade
                if son.cost > maxdepth:
                    maxdepth = son.cost

        # Gravando a variável de maior fronteira
        if len(edge) > maxfrontier: 
            maxfrontier = len(edge)
        
        
    return {"node": None, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": len(edge), "scanned": len(explored)}


def dfs(problem:Problem):
    maxdepth = 0
    maxfrontier = 0
    # Criando o primeiro nó
    node = Node(problem.initial_state, 0)

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
            son = Node(newstate, node.cost + 1, action, node)
            
            # Checa se o filho já foi explorado
            if str(son.state) not in explored:
                # Se o filho for a resposta, retorna a solução
                if problem.objective_test(son.state):
                    return {"node": son, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": len(edge), "scanned": len(explored)}

                # Adiciona o filho a fila e na lista de explorados
                edge.append(son)
                explored.add(str(son.state))

                # Gravando a variável de maior profundidade
                if son.cost > maxdepth:
                    maxdepth = son.cost

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
        node = Node(problem.initial_state, 0)

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
                son = Node(newstate, node.cost + 1, action, node)
                
                # Checa se o filho já foi explorado
                if str(son.state) not in explored:
                    # Se o filho for a resposta, retorna a solução
                    if problem.objective_test(son.state):
                        return {"node": son, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": len(edge), "scanned": len(explored)}

                    # Adiciona o filho a fila e na lista de explorados
                    edge.append(son)
                    explored.add(str(son.state))

                    # Gravando a variável de maior profundidade
                    if son.cost > maxdepth:
                        maxdepth = son.cost

            # Gravando a variável de maior fronteira
            if len(edge) > maxfrontier: 
                maxfrontier = len(edge)
        
        
    return {"node": None, "maxdepth": maxdepth, "maxfrontier": maxfrontier, "finalfrontier": len(edge), "scanned": len(explored)}