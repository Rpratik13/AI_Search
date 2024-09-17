from tree.tree import Tree
from graph import nodes_map
from data_structure.stackImpl import Stack


def DFS(
    initial_state: str,
    goal_state: str,
    print_tree: bool,
) -> list[str]:
    """
    Implements depth first search to go from initial state to goal state.

    Args:
        initial_state (str): The state to start from.
        goal_state (str): The last state to reach.
        print_tree (bool): Decides if state tree is to be printed.

    Returns:
        list[str]: The list of nodes in the path from initial state to goal state.
    """

    stack = Stack()
    tree = Tree()

    nodes_expanded_count = 0

    stack.push((initial_state, []))

    tree.add_node(initial_state, [], 0)

    while True:
        current_item = stack.pop()

        state = current_item[0]  # Node name

        if state in current_item[1]:
            continue

        path_to_state = [*current_item[1], state]

        nodes_expanded_count += 1

        if state == goal_state:
            if print_tree:
                tree.set_goal(path_to_state)
                tree.print()

            break

        neighbors = nodes_map[state]

        for neighbor in sorted(list(neighbors.keys())):
            stack.push((neighbor, path_to_state))

        for neighbor in sorted(list(neighbors.keys()), reverse=True):
            tree.add_node(neighbor, [*current_item[1], state], None)

    return (path_to_state, nodes_expanded_count)
