# Working with Queues

## Introduction to Queues

- Queues follow the FIFI principle: first in, first out.
- This means the first inserted item is the first to be removed, like at a supermarket queue. The first person to
  enter the queue is also the first one to leave.

## Features of Queues

- The beginning of the queue is called the head, the end is called the tail.
- We can only insert data at the end of the queue.
    - This operation is called _enqueue_
- We can only remove from the head of the queue
    - This operation is called _dequeue_
- Other kinds of queues:
    - Doublly ended queues
    - Circular queues
    - Priority queues

## Real-World Use Cases of Queues

- Printing tasks in a printer
    - Documents are printed in the order they are received.
- Applications where the order of requests matters
    - Tickers for a concert
    - Taxi services

## Queues - Implementation

```python
class Node:
    def __init__(self, data):
        self.data = data,
        self.next = None


class Queue:
    def __init__(self):
        self.head = None,
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head:
            current_node = self.head
            self.head = current_node.next
            current_node.next = None
            if self.head is None:
                self.tail = None
```

In Python, the `queue` module offers the Queue and SimpleQueue classes

```python
import queue

orders_queue = queue.SimpleQueue()

orders_queue.put("Sushi")
orders_queue.put("Lasagna")
orders_queue.put("Paella")
```

And we can get the elements in the queue using `orders_queue.get()`. We can get the size of the queue (number of
elements in the queue) using `orders_queue.qsize()`. We can also check if the queue is empty by checking
orders_queue.empty().



