from tree.tree import Tree
from graph import nodes_map
from data_structure.queueImpl import Queue


def BFS(
    initial_state: str,
    goal_state: str,
    print_tree: bool,
) -> list[str]:
    """
    Implements breadth first search to go from initial state to goal state.

    Args:
        initial_state (str): The state to start from.
        goal_state (str): The last state to reach.
        print_tree (bool): Decides if state tree is to be printed.

    Returns:
        list[str]: The list of nodes in the path from initial state to goal state.
    """

    queue = Queue()
    tree = Tree()

    queue.enqueue((initial_state, []))

    while True:
        current_item = queue.dequeue()
        state = current_item[0]  # State name

        path_to_state = [*current_item[1], state]  # Path to the state

        cost = (
            nodes_map[current_item[1][-1]][state]
            if len(current_item)
            and len(current_item[1])
            and current_item[1][-1] in nodes_map
            else None
        )

        tree.add_node(state, current_item[1], cost)

        if state == goal_state:
            break

        for neighbor in nodes_map[state]:
            queue.enqueue((neighbor, path_to_state))

    if print_tree:
        tree.set_goal(path_to_state)
        tree.print()

    return path_to_state
