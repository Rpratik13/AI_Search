import draw


class TreeNode:
    def __init__(self, name, depthPosition=1, cost=None):
        self.name = name
        self.parent = None
        self.depthPosition = depthPosition
        self.children = []
        self.isGoal = 0
        self.cost = cost

    def __repr__(self):
        return f"Tree Node: {self.name}"

    def addChild(self, child):
        self.children.append(child)
        child.parent = self

    def findChild(self, name):
        for child in self.children:
            if child.name == name:
                return child

    def setGoal(self):
        self.isGoal = 1

        if self.parent is not None:
            self.parent.setGoal()


class Tree:
    def __init__(self, root):
        self.root = root
        self.depth = 1
        self.maxBranching = 0
        self.nodesInDepth = {
            0: 1,
        }

    def addNode(self, name, pathArg, cost):
        path = [*pathArg]
        depth = 1
        currentNode = self.root

        path.pop(0)

        while len(path) != 0:
            depth += 1
            item = path.pop(0)

            currentNode = currentNode.findChild(item)

        if depth in self.nodesInDepth:
            self.nodesInDepth[depth] += 1
        else:
            self.nodesInDepth[depth] = 1

        newNode = TreeNode(name, self.nodesInDepth[depth], cost)
        currentNode.addChild(newNode)

        self.depth = max(self.depth, depth)
        self.maxBranching = max(self.maxBranching, len(currentNode.children))

    def print(self):
        currentNode = self.root
        nodes = []
        currentHeight = draw.starting_y

        for depth in self.nodesInDepth:
            for i in range(self.nodesInDepth[depth]):
                draw.createBox(currentNode.name, currentNode.isGoal, currentNode.cost)
                if currentNode.parent is not None:
                    parentX = -(
                        self.nodesInDepth[depth - 1]
                        * (draw.box_length + draw.x_padding)
                        - draw.x_padding
                        - draw.box_length
                    ) / 2 + (currentNode.parent.depthPosition - 1) * (
                        draw.box_length + draw.x_padding
                    )
                    parentY = currentHeight + draw.y_padding

                    draw.drawLine(parentX, parentY)

                nodes = [*nodes, *currentNode.children]
                if len(nodes) == 0:
                    break

                currentNode = nodes.pop(0)

                draw.moveX(draw.box_length + draw.x_padding)

            currentHeight -= draw.y_padding + draw.box_height

            if depth + 1 in self.nodesInDepth:
                draw.move(
                    -(
                        (
                            self.nodesInDepth[depth + 1]
                            * (draw.box_length + draw.x_padding)
                            - draw.x_padding
                            - draw.box_length
                        )
                        / 2
                    ),
                    currentHeight,
                )

        draw.done()

    def addGoal(self, pathToGoalArg):
        if None in pathToGoalArg:
            return

        pathToGoal = [*pathToGoalArg]

        current = self.root

        if len(pathToGoal):
            current.isGoal = True

        pathToGoal.pop(0)

        while len(pathToGoal):
            child = pathToGoal.pop(0)

            current = current.findChild(child)

            if current:
                current.isGoal = True
