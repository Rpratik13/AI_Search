import math

from tree.tree import Tree
from graph import nodes_map, bucharest_sld_map
from data_structure.priorityQueueImpl import PriorityQueueItem, PriorityQueue


def generate_sld_relative_bucharest(goal_state: str) -> dict[str, int]:
    """
    Generates the straight line distance between each node and goal state by
    using straight line distance with Bucharest.

    Args:
        goal_state (str): Node from which straight line distance is to be
        calculated.

    Returns:
        dict[str, int]: Map representing straight line distance between goal the
        each node.
    """

    if goal_state == "Bucharest":
        return {node[0]: node[1][0] for node in list(bucharest_sld_map.items())}

    output = {
        goal_state: 0,
    }

    for node in list(nodes_map.keys()):
        if node in output:
            continue

        angle = abs(bucharest_sld_map[node][1] - bucharest_sld_map[goal_state][1])
        angle = 360 - angle if angle >= 180 else angle

        output[node] = int(
            math.floor(
                math.sqrt(  # Cosine Rule
                    (bucharest_sld_map[node][0] ** 2)
                    + (bucharest_sld_map[goal_state][0] ** 2)
                    - (
                        2
                        * bucharest_sld_map[goal_state][0]
                        * bucharest_sld_map[node][0]
                        * math.cos(angle * math.pi / 180)
                    )
                )
            )
        )

    return output


def generate_sld(goal_state: str) -> dict[str, int]:
    """
    Generates the straight line distance between each node and goal state by
    using triangle inequality.

    Args:
        goal_state (str): Node from which straight line distance is to be
        calculated.

    Returns:
        dict[str, int]: Map representing straight line distance between goal the
        each node.
    """

    output = {
        goal_state: 0,
    }

    nodes_to_expand = []

    neighbors = nodes_map[goal_state]

    for neighbor in neighbors:
        output[neighbor] = neighbors[neighbor]
        nodes_to_expand.append(neighbor)

    while len(nodes_to_expand) != 0:
        node_name = nodes_to_expand.pop(0)
        neighbors = nodes_map[node_name]

        for neighbor in neighbors:
            if neighbor in output:
                continue

            upper_bound = output[node_name] + neighbors[neighbor]
            lower_bound = abs(output[node_name] - neighbors[neighbor])

            sld = lower_bound + 0.7 * (upper_bound - lower_bound)

            output[neighbor] = int(math.floor(sld))

            nodes_to_expand.append(neighbor)

    return output


def a_star_search(
    initial_state: str,
    goal_state: str,
    heuristic: dict[str, int],
    print_tree: bool,
):
    """
    Implements a star search to go from initial state to goal state.

    Args:
        initial_state (str): The state to start from.
        goal_state (str): The last state to reach.
        heuristic_map (dict[str, int]): The map to use for calculating shortest
        distance to goal.
        print_tree (bool): Decides if state tree is to be printed.

    Returns:
        list[str]: The list of nodes in the path from initial state to goal state.
    """
    to_visit = PriorityQueue()
    tree = Tree()

    nodes_expanded_count = 0

    least_path_cost = {
        initial_state: 0,
    }

    path_to_state = {
        initial_state: [initial_state],
    }

    to_visit.enqueue(initial_state, [], 1, 0)

    tree.add_node(initial_state, [], 0)

    while len(to_visit.queue):
        current_node = to_visit.dequeue()

        nodes_expanded_count += 1

        if current_node.name == goal_state:
            if print_tree:
                tree.set_goal(path_to_state[goal_state])
                tree.print()

            return (path_to_state[goal_state], nodes_expanded_count)

        tree_nodes_to_add = []

        for neighbor in nodes_map[current_node.name]:

            actual_path_cost = (
                current_node.cost + nodes_map[current_node.name][neighbor]
            )
            heuristic_path_cost = actual_path_cost + heuristic[neighbor]

            tree_nodes_to_add.append(
                (
                    neighbor,
                    [*current_node.path_to_state, current_node.name],
                    heuristic_path_cost,
                )
            )

            if (
                neighbor not in least_path_cost
                or least_path_cost[neighbor] > actual_path_cost
            ):
                to_visit.enqueue(
                    neighbor,
                    [*current_node.path_to_state, current_node.name],
                    heuristic_path_cost,
                    actual_path_cost,
                )
                path_to_state[neighbor] = [
                    *current_node.path_to_state,
                    current_node.name,
                    neighbor,
                ]
                least_path_cost[neighbor] = actual_path_cost

        for node in sorted(tree_nodes_to_add, key=lambda x: x[2]):
            tree.add_node(node[0], node[1], node[2])
