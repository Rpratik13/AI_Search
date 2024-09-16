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

    queue.enqueue(initial_state, [], 1)

    while True:
        current_item = queue.dequeue()

        cost = (
            nodes_map[current_item.path_to_state[-1]][current_item.name]
            if len(current_item.path_to_state)
            and current_item.path_to_state[-1] in nodes_map
            else None
        )

        tree.add_node(current_item.name, current_item.path_to_state, cost)

        if current_item.name == goal_state:
            break

        if current_item.name in current_item.path_to_state:
            continue

        for neighbor in sort_neighbors_by_cost(nodes_map[current_item.name]):
            queue.enqueue(
                neighbor[0],
                [*current_item.path_to_state, current_item.name],
                maxDepth - len(current_item.path_to_state),
            )

    if print_tree:

        tree.set_goal([*current_item.path_to_state, current_item.name])
        tree.print()

    return [*current_item.path_to_state, current_item.name]
