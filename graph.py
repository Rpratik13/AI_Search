"""
A graph that defines the distance between each of the nodes and its neighbors
"""

nodes_map: dict[str, dict[str, int]] = {
    "Arad": {
        "Sibiu": 140,
        "Timisoara": 118,
        "Zerind": 75,
    },
    "Bucharest": {
        "Fagaras": 211,
        "Giurgiu": 90,
        "Pitesti": 101,
        "Urziceni": 85,
    },
    "Craiova": {
        "Dobreta": 120,
        "Pitesti": 138,
        "Rimnicu Vilcea": 146,
    },
    "Dobreta": {
        "Craiova": 120,
        "Mehadia": 75,
    },
    "Eforie": {
        "Hirsova": 86,
    },
    "Fagaras": {
        "Bucharest": 211,
        "Sibiu": 99,
    },
    "Giurgiu": {
        "Bucharest": 90,
    },
    "Hirsova": {
        "Eforie": 86,
        "Urziceni": 98,
    },
    "Iasi": {
        "Neamt": 87,
        "Vaslui": 92,
    },
    "Lugoj": {
        "Mehadia": 70,
        "Timisoara": 111,
    },
    "Mehadia": {
        "Dobreta": 75,
        "Lugoj": 70,
    },
    "Neamt": {
        "Iasi": 87,
    },
    "Oradea": {
        "Sibiu": 151,
        "Zerind": 71,
    },
    "Pitesti": {
        "Bucharest": 101,
        "Craiova": 138,
        "Rimnicu Vilcea": 97,
    },
    "Rimnicu Vilcea": {
        "Craiova": 146,
        "Pitesti": 97,
        "Sibiu": 80,
    },
    "Sibiu": {
        "Arad": 140,
        "Fagaras": 99,
        "Oradea": 151,
        "Rimnicu Vilcea": 80,
    },
    "Timisoara": {
        "Arad": 118,
        "Lugoj": 111,
    },
    "Urziceni": {
        "Bucharest": 85,
        "Hirsova": 98,
        "Vaslui": 142,
    },
    "Vaslui": {
        "Iasi": 92,
        "Urziceni": 142,
    },
    "Zerind": {
        "Arad": 75,
        "Oradea": 71,
    },
}

"""
Map describing the straight line distance between each nodes and Bucharest
"""
bucharest_sld_map: dict[str, int] = {
    "Arad": (366, 160),
    "Bucharest": (0, 0),
    "Craiova": (160, 195),
    "Dobreta": (242, 190),
    "Eforie": (161, 350),
    "Fagaras": (176, 125),
    "Giurgiu": (77, 247),
    "Hirsova": (151, 10),
    "Iasi": (226, 70),
    "Lugoj": (244, 165),
    "Mehadia": (241, 175),
    "Neamt": (234, 90),
    "Oradea": (380, 140),
    "Pitesti": (100, 152),
    "Rimnicu Vilcea": (193, 155),
    "Sibiu": (253, 147),
    "Timisoara": (329, 165),
    "Urziceni": (80, 25),
    "Vaslui": (199, 45),
    "Zerind": (374, 145),
}
