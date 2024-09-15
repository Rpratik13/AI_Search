from typing import Any


class Queue:
    """
    Implementation of a Queue data structure.

    Attributes:
        queue (list[any]): Maintains the items in the queue.

    Methods:
        enqueue() -> None:
            Adds item to the end of the queue.
        dequeue() -> any:
            Extracts item from the front of the queue. Raises Exception if queue is empty.
    """

    def __init__(self):
        self.queue: list[Any] = []

    def __repr__(self):
        return self.queue

    def enqueue(self, item: Any) -> None:
        """
        Adds item to the end of a queue.

        Args:
            item (Any): The item to be inserted to the queue.

        Returns:
            None: This function does not return anything.
        """

        self.queue.append(item)

    def dequeue(self) -> Any:
        """
        Extracts item from the front of the queue.

        Returns:
            Any: The item at the front of the queue.

        Raises:
            Exception: If queue is empty.
        """

        if len(self.queue) == 0:
            raise Exception("Queue is empty")

        return self.queue.pop(0)
