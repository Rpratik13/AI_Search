from queue import Queue
from tree import Tree, TreeNode
from graph import nodesMap


initialState = "Arad"
goalState = "Bucharest"


def BFS(initialState: str, goalState: str):
    nodeExpandedCount = 0

    queue = Queue()
    tree = Tree(TreeNode(initialState))
    state = None

    queue.enqueue((initialState, []))

    while True:
        currentItem = queue.dequeue()
        state = currentItem[0]
        pathToState = [*currentItem[1], state]
        nodeExpandedCount += 1

        if state == goalState:
            break

        neighbors = nodesMap[state]

        for neighbor in neighbors:
            queue.enqueue((neighbor, pathToState))

            tree.addNode(neighbor, pathToState, nodesMap[state][neighbor])

    tree.addGoal(pathToState)

    print(pathToState)

    tree.print()

    return nodeExpandedCount


print(BFS(initialState, goalState))
