import math

from tree.tree import Tree
from graph import nodes_map, bucharest_sld_map


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
        return bucharest_sld_map

    output = {
        goal_state: 0,
    }

    nodes_to_expand = []

    for neighbor in nodes_map[goal_state]:
        output[neighbor] = neighbors[neighbor]
        nodes_to_expand.append(neighbor)

    while len(nodes_to_expand):
        node_name = nodes_to_expand.pop(0)
        neighbors = nodes_map[node_name]

        for neighbor in neighbors:
            if neighbor in output:
                continue

            sld = (output[node_name] ** 2 + neighbors[neighbor] ** 2) ** 0.5

            if sld > output[node_name] + neighbors[neighbor]:
                sld -= sld - (output[node_name] + neighbors[neighbor]) - 10
            elif sld < abs(output[node_name] - neighbors[neighbor]):
                sld += sld - abs(output[node_name] + neighbors[neighbor]) + 10

            output[neighbor] = int(math.floor(sld))

            nodes_to_expand.append(neighbor)

    return output


def generate_sld(goal_state: str) -> dict[str, int]:
    """
    Generates the straight line distance between each node and goal state by
    using triangle inequality and pythagoras theorem.

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

            sld = (output[node_name] ** 2 + neighbors[neighbor] ** 2) ** 0.5

            if sld > output[node_name] + neighbors[neighbor]:
                sld -= sld - (output[node_name] + neighbors[neighbor]) - 10
            elif sld < abs(output[node_name] - neighbors[neighbor]):
                sld += sld - abs(output[node_name] + neighbors[neighbor]) + 10

            output[neighbor] = int(math.floor(sld))

            nodes_to_expand.append(neighbor)

    return output


def a_star_search(
    initial_state: str,
    goal_state: str,
    heuristic_map: dict[str, int],
    print_tree: bool,
) -> list[str]:
    """
    Implements breadth first search to go from initial state to goal state.

    Args:
        initial_state (str): The state to start from.
        goal_state (str): The last state to reach.
        heuristic_map (dict[str, int]): The map to use for calculating shortest
        distance to goal.
        print_tree (bool): Decides if state tree is to be printed.

    Returns:
        list[str]: The list of nodes in the path from initial state to goal state.
    """

    state = initial_state
    path_to_state = [state]
    next_state = None
    distance_to_next_state = float("inf")
    total_distance = 0

    tree = Tree()
    tree.add_node(initial_state, [], None)

    while state != goal_state:
        for neighbor in nodes_map[state]:
            distance_to_next_stateFromNode = (
                total_distance + nodes_map[state][neighbor] + heuristic_map[neighbor]
            )

            tree.add_node(
                neighbor,
                path_to_state,
                total_distance + nodes_map[state][neighbor] + heuristic_map[neighbor],
            )

            if (
                distance_to_next_stateFromNode < distance_to_next_state
                and neighbor not in path_to_state
            ):
                distance_to_next_state = distance_to_next_stateFromNode

                next_state = neighbor

        total_distance += nodes_map[state][neighbor]

        state = next_state
        path_to_state.append(state)
        distance_to_next_state = float("inf")
        next_state = None

    print(path_to_state)

    if print_tree:
        tree.set_goal(path_to_state)
        tree.print()

    return path_to_state
