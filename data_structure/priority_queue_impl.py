class PriorityQueueItem:
    """
    Item to be stored in the priority queue for greedy search.

    Attributes:
        name (str): Name of the node to be stored.
        path_to_state (list[str]): The path taken from initial state to reach the current state.
        priority (int): The priority order in which the item is to be stored.
        cost (int): The cost to reach the node
    """

    def __init__(
        self, name: str, path_to_state: list[str], priority: int, cost: int = 0
    ):
        self.name = name
        self.path_to_state = path_to_state
        self.priority = priority
        self.cost = cost

    def __repr__(self):
        return f"{self.name}, {self.priority}"


class PriorityQueue:
    """
    Implementation of a Priority Queue data structure.

    Attributes:
        queue (list[PriorityQueueItem]): Maintains the items in the queue.

    Methods:
        enqueue() -> None:
            Adds item to the queue based on the priority order.
        dequeue() -> Any:
            Removes item from the start of the queue. Raises Exception if queue is empty.
    """

    def __init__(self):
        self.queue: list[PriorityQueueItem] = []

    def __repr__(self):
        return self.queue.join(",")

    def enqueue(
        self, name: str, path_to_state: list[str], priority: int, cost: int = 0
    ) -> None:
        """
        Adds item to the queue based on the priority order.

        Args:
            name (str): Name of the node to be inserted.
            path_to_state (list[str]): The path taken from the initial state to reach current state.
            priority (int): The priority order in which the item is to be stored.
            cost (int): The cost to reach the node

        Returns:
            None: This function does not return anything.
        """

        index_for_new_item = 0

        for index in range(len(self.queue)):
            if self.queue[index].priority >= priority:
                break

            index_for_new_item += 1

        self.queue = (
            self.queue[:index_for_new_item]
            + [PriorityQueueItem(name, path_to_state, priority, cost)]
            + self.queue[index_for_new_item:]
        )

    def dequeue(self) -> PriorityQueueItem:
        """
        Extracts item from the start of the queue.

        Returns:
            PriorityQueueItem: The item at the start of the queue.

        Raises:
            Exception: If queue is empty.
        """

        if len(self.queue) == 0:
            raise Exception("Queue is empty")

        return self.queue.pop(0)
