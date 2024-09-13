from graph import nodesMap
from tree import Tree, TreeNode
from priorityQueue import PriorityQueue


initialState = "Sibiu"
goalState = "Fagaras"

maxDepth = len(nodesMap.keys())


def sortNeighborsByCost(neighbors):
    return sorted(neighbors.items(), key=lambda x: x[1], reverse=True)


def greedySearch(initialState: str, goalState: str):
    nodeExpandedCount = 0

    tree = Tree(TreeNode(initialState))
    queue = PriorityQueue()

    queue.enqueue(initialState, [], 1)

    while True:
        currentItem = queue.dequeue()

        if currentItem.name == goalState:
            break

        if currentItem.name in currentItem.pathToState:
            continue

        nodeExpandedCount += 1

        neighbors = nodesMap[currentItem.name]

        for neighbor in sortNeighborsByCost(neighbors):

            queue.enqueue(
                neighbor[0],
                [*currentItem.pathToState, currentItem.name],
                maxDepth - len(currentItem.pathToState),
            )

            print(neighbor[0], [*currentItem.pathToState, currentItem.name])
            tree.addNode(
                neighbor[0],
                [*currentItem.pathToState, currentItem.name],
                nodesMap[currentItem.name][neighbor[0]],
            )

    tree.addGoal([*currentItem.pathToState, currentItem.name])
    tree.print()

    return nodeExpandedCount


print(greedySearch(initialState, goalState))
