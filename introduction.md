# Introduction

## The importance of algorithms and data structures

- Data structures and algorithms enable us to
    - solve every day problems
    - using efficient code
- This course is in Python but the skills are transferable

## Algorithms and data structures

- Algorithm: set of instructions that solve a problem
- First we design them, then we code them.
- Data structures hold and manipulate data when we execute analgorithm
    - We will cover advanced data structures: linked lists, stacks, queues...

## Linked List

A linked list is a sequence of data connected through links. Each element is called a node. Each node contains data,
with a pointer to the next node, with the pointer of the final node pointing to null.The first node is called the head,
the final node is called the tail.

The data in a linked list does not need to be stored in contiguous blocks of memory, meaning the data can be stored in
any available memory address.

If every node has only one link, it is called a singly linked list. If each node has two links in either direction, it
is called a doubly linked list. Linked lists can be used to implement other data structures like stacks, queues, and
graphs.

A common usage of linked lists is to access information by navigating forward and backward.

Let's implement a node by defining a class:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

The `__init__` method is called every time the class is instantiated. The `data` property contains the data for the
node, and `next` points to the next node. Initially, `next` points to None.

Next we define a new `LinkedList` class which will eventually contain nodes.

```python
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
```

We can now implement different methods to insert or remove nodes at different positions of the linked list, or to search
for a value in the linked list:

- `insert_at_beginning()`
- `remove_at_beginning()`
- `insert_at_end()`
- `remove_at_end()`
- `insert_at()`
- `remove_at()`
- `search()`

Let's implement the `insert_at_beginning()` method, to insert a new node at the beginning of a linked list. For this, we
first create a new node. Then we check if the linked list is empty by checking if there is a head node. If there is, the
new node points to it and the new node becomes the head. If the linked list is empty, so the new node we are creating is
the only link in our linked list, then it is both the head and the tail.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node
```

We can now implement the `insert_at_end()` method. Again, we will first have to define a new node. First we check if the
linked is not empty (so contains nodes). If this is True, then the tail of the previous node will point to the new node,
while the new node becomes the new tail. If the linked list is empty, then the new node, again, becomes both the head
and the tail.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node
```

The last method we will implement, will search for a given value in a linked list.

We start our search at the first node. While we still have nodes to visit, we check whether the data of the node we are
currently on contains the data we are looking for and return True, else we move to the next node, like a train moving
along the tracks. If we never find our data even after reaching the tail, we must return False.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False
```

With this, we can find the stray sushi roll! See `linked_list_code.py`.