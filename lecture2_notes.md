# Working with Stacks

## Stacks

Stacks follow the LIFO principle, last in first out. That means, the last inserted item will be the first element which
can be removed. When we add to the stack, this is called pushing onto the stack. When we remove from the top of the
stack, this is called popping from the stack. We can only read the last-added element on the stack, and this is called
peeking from the stack.

## Real Use-Cases of Stacks

- The undo functionality in a word processor. We can push onto the stack each key press the user types. When the user
  makes a mistake and wants to undo it, we pop the last inserted keystroke from the stack.
- The symbol checker in a coding platform. When a user opens a bracket, we push it onto the stack. Then we check for the
  closing symbol, and if it exists, we pop the existing opening symbol from the stack. If there are still elements left
  in the stack, then we will know the user has not closed (or opened) the brackets.

### Stacks - Implementation using Singly Linked Lists

Stacks can be implemented using singly linked lists. Linked lists have nodes - as previously defined

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

As previously, each node contains data and a pointer to the next node. Now we will implement a class for the stack:

```python
class Stack:
    def __init__(self):
        self.top = None
```

Initially, the top node will be none. If we want to push new elements to our stack, we will need a push method:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node
```

If we want to pop elements from our stack, we can also define a pop node:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data
```

If we want to define a peek method, that would look like this:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None
```

Instead of creating a stack outselves each time, we can use `queue`, python's lifoqueue module. We can create a new Lifo
Queue using `queue` like so:

```python
import queue

# To put to the stack
my_book_stack = queue.LifoQueue(maxsize=0)
my_book_stack.put("A man for all markets")
my_book_stack.put("Beat the dealer")
my_book_stack.put("The predictors")

# To get from the stack
my_book_stack.get()

# To empty the stack
my_book_stack.empty()
```

