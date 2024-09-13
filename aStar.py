import math

from graph import createGraph, Graph, nodesMapDefault
from tree import Tree, TreeNode

initialState = "Arad"
goalState = "Bucharest"

graph = createGraph()


def generateSLD(goalState):
    output = {
        goalState: 0,
    }

    nodesToExpand = []

    currentNode = graph.findNode(goalState)
    neighbors = currentNode.getNeighbors()

    for neighbor in neighbors:
        output[neighbor] = neighbors[neighbor]
        nodesToExpand.append(neighbor)

    while len(nodesToExpand) != 0:
        nodeName = nodesToExpand.pop(0)
        node = graph.findNode(nodeName)

        neighbors = node.getNeighbors()

        for neighbor in neighbors:
            if neighbor in output:
                continue

            sld = (output[nodeName] ** 2 + neighbors[neighbor] ** 2) ** 0.5

            if sld > output[nodeName] + neighbors[neighbor]:
                sld -= sld - (output[nodeName] + neighbors[neighbor]) - 10
            elif sld < abs(output[nodeName] - neighbors[neighbor]):
                sld += sld - abs(output[nodeName] + neighbors[neighbor]) + 10

            output[neighbor] = int(math.floor(sld))

            nodesToExpand.append(neighbor)

    return output


generateSLD(goalState)


def aStarSearch(
    graph: Graph, initialState: str, goalState: str, heuristicMap: dict[str, int]
):
    nodeExpandedCount = 0

    state = initialState
    pathToState = [state]
    nextState = None
    distanceToNextState = float("inf")
    totalDistance = 0

    tree = Tree(TreeNode(initialState))

    while state != goalState:
        nodeExpandedCount += 1

        node = graph.findNode(state)
        neighbors = node.getNeighbors()

        for neighbor in neighbors:

            distanceToNextStateFromNode = (
                totalDistance
                + nodesMapDefault[state][neighbor]
                + heuristicMap[neighbor]
            )

            tree.addNode(
                neighbor,
                pathToState,
                totalDistance
                + nodesMapDefault[state][neighbor]
                + heuristicMap[neighbor],
            )

            if (
                distanceToNextStateFromNode < distanceToNextState
                and neighbor not in pathToState
            ):
                distanceToNextState = distanceToNextStateFromNode

                nextState = neighbor

        totalDistance += nodesMapDefault[state][neighbor]

        state = nextState
        pathToState.append(state)
        distanceToNextState = float("inf")
        nextState = None

    tree.addGoal(pathToState)
    tree.print()
    print(pathToState)
    return nodeExpandedCount


print(generateSLD(goalState))
print(aStarSearch(graph, initialState, goalState, generateSLD(goalState)))
