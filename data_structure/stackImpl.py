from typing import Any


class Stack:
    """
    Implementation of a stack data structure.

    Attributes:
        stack (list[Any]): Maintains the items in the stack.

    Methods:
        push() -> None:
            Adds item to the top of the stack.
        pop() -> Any:
            Removes item from the top of the stack. Raises Exception if stack is empty.
    """

    def __init__(self):
        self.stack: list[Any] = []

    def __repr__(self):
        return self.stack

    def push(self, item: Any) -> None:
        """
        Adds item to the top of the stack.

        Args:
            item (Any): The item to be inserted to the stack.

        Returns:
            None: This function does not return anything.
        """

        self.stack.append(item)

    def pop(self) -> Any:
        """
        Extract item from the top of the stack.

        Returns:
            Any: The item at the top of the stack.

        Raises:
            Exception: If stack is empty.
        """

        if len(self.stack) == 0:
            raise Exception("Stack is empty")

        return self.stack.pop()
