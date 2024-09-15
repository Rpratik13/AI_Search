import tree.draw as draw


class TreeNode:
    """
    Implementation of a tree node for each state of search tree.

    Attributes:
        name (str): Name of the node.
        depth (int): Depth of the node in the tree.
        cost (int): Cost from previous node to reach current node.
        parent (TreeNode): Parent node of the current node.
        is_goal (bool): Determines if current node is part of the path from
        initial state to goal state.
        children (dict[str], TreeNode): Children nodes of the current node.
        position_in_depth (int): The index of the node in the its depth.

    Methods:
        add_child(node: TreeNode) -> None:
            Adds a child to current node.
        find_child(name: str) -> TreeNode:
            Finds the child with given name.
        set_goal() -> Node:
            Marks the node as part of the goal path.
    """

    def __init__(
        self,
        name,
        depth=0,
        cost=None,
        parent=None,
        is_goal=False,
        position_in_depth=0,
    ):
        self.name = name
        self.depth = depth
        self.cost = cost
        self.parent = parent
        self.is_goal = is_goal
        self.children = {}
        self.position_in_depth = position_in_depth

    def __repr__(self):
        return f"Tree Node: {self.name}"

    def add_child(self, node):
        """
        Adds a child to current node.

        Returns:
            None: This function does not return anything.
        """

        self.children[node.name] = node

    def find_child(self, name: str):
        """
        Finds the child with given name.

        Returns:
            TreeNode: The child of the current node with given name.
        """

        return self.children[name]

    def set_goal(self) -> None:
        """
        Marks the node as part of the goal path.

        Returns:
            None: This function does not return anything.
        """

        self.is_goal = True


class Tree:
    """
    Implementation of a search tree.

    Attributes:
        root (TreeNode): Root of the tree.
        nodes_in_depth (dict[int, int]): The map counting nodes in each depth of
        the tree.
        nodes (list[TreeNode]): The list nodes present in the tree.

    Methods:
        add_node(name: str, path_to_state_arg: list[str], cost: int) -> None:
            Adds node to the tree.
        print() -> None:
            Prints the tree in turtle.
        set_goal(path_to_state: list[str]) -> Node:
            Marks the nodes in path to state as goal path.
    """

    def __init__(self):
        self.root = None
        self.nodes_in_depth = {}
        self.nodes = []

    def add_node(self, name: str, path_to_state_arg: list[str], cost: int) -> None:
        """
        Adds node to the tree.

        Args:
            name (str): Name of the node.
            path_to_state_arg (list[str]): List of nodes on the path from
            initial state to current node.
            cost (int): The cost from previous node to current node.

        Returns:
            None: This function does not return anything.
        """

        path_to_state = [*path_to_state_arg]
        current_node = self.root

        if current_node is None:
            self.root = TreeNode(name, depth=0)
            self.nodes_in_depth[0] = 1

            self.nodes.append(self.root)

            return

        if len(path_to_state):
            path_to_state.pop(0)

        depth = 1

        while len(path_to_state):
            depth += 1
            next_node = path_to_state.pop(0)

            current_node = current_node.find_child(next_node)

        if depth in self.nodes_in_depth:
            self.nodes_in_depth[depth] += 1
        else:
            self.nodes_in_depth[depth] = 1

        new_node = TreeNode(
            name,
            depth=depth,
            cost=cost,
            parent=current_node,
            position_in_depth=self.nodes_in_depth[depth] - 1,
        )

        current_node.add_child(new_node)
        self.nodes.append(new_node)

    def print(self) -> None:
        """
        Prints the tree in turtle.

        Returns:
            None: This function does not return anything.
        """

        draw.initialize_turtle()

        for node in self.nodes:
            nodeX = -(
                (self.nodes_in_depth[node.depth] - 1)
                * (draw.box_length + draw.x_padding)
            ) / 2 + node.position_in_depth * (draw.box_length + draw.x_padding)

            nodeY = draw.starting_y - node.depth * (draw.box_height + draw.y_padding)

            draw.move(nodeX, nodeY)
            draw.create_box(node.name, node.is_goal, node.cost)

            if node.depth != 0:
                parentX = -(
                    (self.nodes_in_depth[node.depth - 1] - 1)
                    * (draw.box_length + draw.x_padding)
                ) / 2 + node.parent.position_in_depth * (
                    draw.box_length + draw.x_padding
                )

                parentY = (
                    draw.starting_y
                    - (node.depth - 1) * (draw.box_height + draw.y_padding)
                    - draw.box_height
                )

                draw.draw_line(parentX, parentY)

        draw.done()

    def set_goal(self, path_to_state) -> None:
        """
        Marks the nodes in path to state as goal path.

        Args:
            path_to_state (list[str]): List of nodes from initial state to goal
            state.

        Returns:
            None: This function does not return anything.
        """

        current_node = self.root
        current_node.set_goal()

        for i in range(1, len(path_to_state)):
            current_node = current_node.find_child(path_to_state[i])

            current_node.set_goal()
