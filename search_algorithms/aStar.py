import math

from tree.tree import Tree
from graph import nodes_map, bucharest_sld_map


def generate_node_count_map() -> dict[str, int]:
    """
    Generates the number of nodes between each of the nodes in the map.

    Returns:
        dict[str, [str, int]]: Map representing the number of nodes between each
        of the nodes.
    """

    output = {}

    for node in nodes_map:
        output[node] = {
            node: 0,
        }

        node_to_expand = [(i, 1) for i in list(nodes_map[node])]

        while len(node_to_expand):
            current_node = node_to_expand.pop(0)

            if current_node[0] in output[node]:
                continue

            output[node][current_node[0]] = current_node[1]

            for neighbor in nodes_map[current_node[0]]:
                node_to_expand.append((neighbor, current_node[1] + 1))

    return output


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

    node_count_map = generate_node_count_map()

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
            (node_count_map[node][goal_state] * 100)
            + math.floor(
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
            distance_to_next_state_from_node = (
                total_distance + nodes_map[state][neighbor] + heuristic_map[neighbor]
            )

            tree.add_node(
                neighbor,
                path_to_state,
                total_distance + nodes_map[state][neighbor] + heuristic_map[neighbor],
            )

            if (
                distance_to_next_state_from_node < distance_to_next_state
                and neighbor not in path_to_state
            ):
                distance_to_next_state = distance_to_next_state_from_node

                next_state = neighbor

        total_distance += nodes_map[state][neighbor]

        state = next_state
        path_to_state.append(state)
        distance_to_next_state = float("inf")
        next_state = None

    if print_tree:
        tree.set_goal(path_to_state)
        tree.print()

    return path_to_state
