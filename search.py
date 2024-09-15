import argparse

from search_algorithms.bfs import BFS
from search_algorithms.dfs import DFS
from search_algorithms.greedy import greedy_search
from search_algorithms.aStar import (
    generate_sld,
    generate_sld_relative_bucharest,
    a_star_search,
)

from graph import nodes_map

parser = argparse.ArgumentParser(
    description="A script to run AI search algorithms",
)

parser.add_argument(
    "--algorithm",
    type=str,
    choices=["bfs", "dfs", "greedy", "aStar", "aStarBucharestRelative"],
    default="bfs",
    help="The algorithm to use",
)

node_names = list(nodes_map.keys())
parser.add_argument(
    "--initial_state",
    type=str,
    choices=node_names,
    help="The node to start from",
    default="Arad",
)
parser.add_argument(
    "--goal_state",
    type=str,
    choices=node_names,
    help="The node to end on",
    default="Bucharest",
)

parser.add_argument(
    "--print_tree",
    type=bool,
    default=False,
)


args = parser.parse_args()

path_to_state = None

if args.algorithm == "bfs":
    path_to_state = BFS(
        args.initial_state,
        args.goal_state,
        args.print_tree,
    )
elif args.algorithm == "dfs":
    path_to_state = DFS(
        args.initial_state,
        args.goal_state,
        args.print_tree,
    )
elif args.algorithm == "greedy":
    path_to_state = greedy_search(
        args.initial_state,
        args.goal_state,
        args.print_tree,
    )
elif args.algorithm == "aStar":
    path_to_state = a_star_search(
        args.initial_state,
        args.goal_state,
        generate_sld(args.goal_state),
        args.print_tree,
    )
elif args.algorithm == "aStarBucharestRelative":
    path_to_state = a_star_search(
        args.initial_state,
        args.goal_state,
        generate_sld_relative_bucharest(args.goal_state),
        args.print_tree,
    )
