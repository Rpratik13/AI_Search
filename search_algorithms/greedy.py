from tree.tree import Tree
from graph import nodes_map
from data_structure.priorityQueueImpl import PriorityQueue


maxDepth = len(nodes_map.keys())  # Estimate of max depth the search tree could reach


def sort_neighbors_by_cost(neighbors: dict[str, int]) -> list[tuple[str, int]]:
    """
    Sorts the given neighbors by cost to reach them.

    Args:
        neighbors (dict[str, int]): The dictionary of neighbors with name as key and cost as value.

    Returns:
        list[tuple[str, int]]: The list of tuples with name and cost in ascending order of the cost.
    """

    return sorted(neighbors.items(), key=lambda x: x[1], reverse=True)


def greedy_search(
    initial_state: str,
    goal_state: str,
    print_tree: bool,
) -> list[str]:
    """
    Implements greedy search to go from initial state to goal state.

    Args:
        initial_state (str): The state to start from.
        goal_state (str): The last state to reach.
        print_tree (bool): Decides if state tree is to be printed.

    Returns:
        list[str]: The list of nodes in the path from initial state to goal state.
    """

    tree = Tree()
    queue = PriorityQueue()

    nodes_expanded_count = 0

    queue.enqueue(initial_state, [], 1)

    tree.add_node(initial_state, [], 0)

    while True:
        current_item = queue.dequeue()

        nodes_expanded_count += 1

        if current_item.name == goal_state:
            if print_tree:
                tree.set_goal([*current_item.path_to_state, current_item.name])
                tree.print()
                break

        if current_item.name in current_item.path_to_state:
            continue

        tree_nodes_to_add = []

        for neighbor in sort_neighbors_by_cost(nodes_map[current_item.name]):
            queue.enqueue(
                neighbor[0],
                [*current_item.path_to_state, current_item.name],
                maxDepth - len(current_item.path_to_state),
            )

            tree_nodes_to_add.append(
                (
                    neighbor[0],
                    [*current_item.path_to_state, current_item.name],
                    neighbor[1],
                )
            )

        for neighbor in sorted(tree_nodes_to_add, key=lambda x: x[2]):
            tree.add_node(
                neighbor[0],
                neighbor[1],
                neighbor[2],
            )

    return ([*current_item.path_to_state, current_item.name], nodes_expanded_count)
