from stack import Stack
from graph import nodesMap
from tree import Tree, TreeNode

initialState = "Arad"
goalState = "Timisoara"


def DFS(initialState: str, goalState: str):
    nodeExpandedCount = 0

    stack = Stack()
    tree = Tree(TreeNode(initialState))
    state = None

    stack.push((initialState, []))

    while True:
        currentItem = stack.pop()
        state = currentItem[0]

        if state in currentItem[1]:
            continue

        pathToState = [*currentItem[1], state]
        nodeExpandedCount += 1

        if state == goalState:
            break

        neighbors = nodesMap[state]

        for neighbor in neighbors:
            stack.push((neighbor, pathToState))
            tree.addNode(neighbor, pathToState, nodesMap[state][neighbor])

    tree.addGoal(pathToState)
    tree.print()

    print(pathToState)
    return nodeExpandedCount


print(DFS(initialState, goalState))
