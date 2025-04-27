class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return "Queue is empty"

    def display(self):
        print("Queue:", self.queue)

q = Queue()
for val in map(int, input("Enter elements to enqueue: ").split()):
    q.enqueue(val)
q.display()
print("Dequeued:", q.dequeue())
q.display()
