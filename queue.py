class Queue:
    def __init__(self):
        self.queue = []

    def __repr__(self):
        return self.queue

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) == 0:
            raise Exception("Queue is empty")

        return self.queue.pop(0)
