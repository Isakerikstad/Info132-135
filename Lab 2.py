class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def add_at_beggining(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


l = LinkedList()

l.add_at_beggining(1)
l.add(2)
l.print_list()


