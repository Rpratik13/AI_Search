class PriorityQueueItem:
    def __init__(self, name, pathToState, priority):
        self.name = name
        self.pathToState = pathToState
        self.priority = priority

    def __repr__(self):
        return f"{self.name}, {self.priority}"


class PriorityQueue:
    def __init__(self):
        self.queue: list[PriorityQueueItem] = []

    def __repr__(self):
        return self.queue

    def enqueue(self, name, pathToState, priority):
        indexForNewItem = 0

        for index in range(len(self.queue)):
            if self.queue[index].priority < priority:
                indexForNewItem += 1
            else:
                break

        self.queue = (
            self.queue[:indexForNewItem]
            + [PriorityQueueItem(name, pathToState, priority)]
            + self.queue[indexForNewItem:]
        )

    def dequeue(self):
        if len(self.queue) == 0:
            raise Exception("Queue is empty")

        return self.queue.pop(0)
