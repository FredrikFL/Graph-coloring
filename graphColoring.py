import numpy as np

g1 = np.random.randint(0, 4, size=(8, 8))

def newGraph(graph):
    nGraph = np.random.randint(1, 4, size=(len(graph), len(graph[0])))
    for x in range(0, len(graph)):
        for y in range(0, len(graph[0])):
            if(graph[x][y] == 0):
                nGraph[x][y] = 0
    return nGraph

def getNeighbours(graph, x, y):
    if(graph[x][y] == 0):
        return []

    g = []
    if(x < len(graph)-1):
        g.append([x+1, y])          #+1  0
        if(y < len(graph[0])-1):
            g.append([x+1, y+1])    #+1 +1
    if(y < len(graph[0])-1):
        g.append([x, y+1])          #0  +1
        if(x > 0):
            g.append([x-1, y+1])    #-1 +1
    return g

def getPairs(graph, x, y):
    pairs = 0
    p = getNeighbours(graph, x, y)
    for i in p:
        #print(graph[i[0]][i[1]], graph[x][y])
        if(graph[i[0]][i[1]] == graph[x][y]):
            pairs += 1
    #print("Pairs:", pairs)
    return pairs

def getFitness(graph):
    fitness = 0
    for x in range(0, len(graph)):
        for y in range(0, len(graph[0])):
            fitness += getPairs(graph, x, y)
    return fitness

def makeChildren(graph1, graph2):
    x1 = np.random.randint(0, len(graph1))
    x2 = np.random.randint(0, len(graph1))
    y1 = np.random.randint(0, len(graph1))
    y2 = np.random.randint(0, len(graph1))

    if(x1 <= x2):
        for x in range(x1, x2):
            if(y1 <= y2):
                for y in range(y1, y2):
                    temp = graph1[x][y]
                    graph1[x][y] = graph2[x][y]
                    graph2[x][y] = temp
            else:
                for y in range(y2, y1):
                    temp = graph1[x][y]
                    graph1[x][y] = graph2[x][y]
                    graph2[x][y] = temp
    else:
        for x in range(x2, x1):
            if(y1 <= y2):
                for y in range(y1, y2):
                    temp = graph1[x][y]
                    graph1[x][y] = graph2[x][y]
                    graph2[x][y] = temp
            else:
                for y in range(y2, y1):
                    temp = graph1[x][y]
                    graph1[x][y] = graph2[x][y]
                    graph2[x][y] = temp

    return graph1, graph2

def mutation(graph):
    if(np.random.randint(0, 4) == 0):
        x = np.random.randint(0, len(graph))
        y = np.random.randint(0, len(graph))
        if(graph[x][y] != 0):
            graph[x][y] = np.random.randint(1, 4)
    return graph

g = [g1, g1, g1, g1, g1, g1, g1, g1, g1, g1]
g[0] = newGraph(g1)
g[1] = newGraph(g1)
g[2] = newGraph(g1)
g[3] = newGraph(g1)
g[4] = newGraph(g1)
g[5] = newGraph(g1)
g[6] = newGraph(g1)
g[7] = newGraph(g1)
g[8] = newGraph(g1)
g[9] = newGraph(g1)

fitness = getFitness(g[0])
print(g[0])
print("Fitness:", getFitness(g[0]))

lastImprovment = 0

gen = [('graph', int, (8,8)), ('fitness', int)]
temp = [(g[0], getFitness(g[0])),
        (g[1], getFitness(g[1])),
        (g[2], getFitness(g[2])),
        (g[3], getFitness(g[3])),
        (g[4], getFitness(g[4])),
        (g[5], getFitness(g[5])),
        (g[6], getFitness(g[6])),
        (g[7], getFitness(g[7])),
        (g[8], getFitness(g[8])),
        (g[9], getFitness(g[9]))]

parents  = np.array(temp, dtype=gen)
children = np.zeros(20, dtype=gen)

fitness = getFitness(g[0])

np.sort(parents, order="fitness")

while(lastImprovment < 50):

    fit = parents[0]["fitness"]
    if fit < fitness:
        print("improvment", fitness - fit, lastImprovment)
        fitness = fit
        best    = parents[0]
        lastImprovment = 0
        #print(best)

    for i in range(0, len(parents)-1):
        children[2*i]["graph"], children[2*i+1]["graph"] = makeChildren(parents[i]["graph"], parents[i+1]["graph"])
        children[2*i]["fitness"]   = getFitness(children[2*i]["graph"])
        children[2*i+1]["fitness"] = getFitness(children[2*i+1]["graph"])
    children[len(children)-1]["graph"], children[len(children)-2]["graph"] = makeChildren(parents[0]["graph"], parents[len(parents)-1]["graph"])
    children[len(children)-1]["fitness"] = getFitness(children[len(children)-1]["graph"])
    children[len(children)-2]["fitness"] = getFitness(children[len(children)-2]["graph"])

    np.sort(children, order="fitness")
    parents[0:9] = children[0:9]
    m = np.random.randint(0, len(parents)-1)
    parents[m]["graph"] = mutation(parents[m]["graph"])

    lastImprovment += 1
    #print(fitness)


print(best["graph"])
print("Fitness:", fitness)
