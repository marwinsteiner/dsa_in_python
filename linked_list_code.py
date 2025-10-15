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
                print("data found")
                return True
            else:
                current_node = current_node.next
        print("no data found")
        return False

if __name__ == '__main__':
    sushi_preparation = LinkedList()

    # Insert values
    sushi_preparation.insert_at_end("prepare")
    sushi_preparation.insert_at_end("roll")
    sushi_preparation.insert_at_beginning("assemble")

    # Search for values
    print("searching for roll")
    sushi_preparation.search("roll")
    print("searching for prepare")
    sushi_preparation.search("prepare")
    print("searching for mixing")
    sushi_preparation.search("mixing")