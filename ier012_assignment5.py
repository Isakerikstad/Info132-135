#Assignment 5 Isak Erikstad

#Oppgave 1
"All of the following trees are full binary trees"

#Oppgave 2

def binary_tree(r):
    return [r, [], []]

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

def insert_left_child(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right_child(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root

def make_tree():
    global my_tree
    my_tree = binary_tree(1)
    insert_left_child(my_tree, 2)
    insert_right_child(my_tree, 3)
    insert_left_child(get_left_child(my_tree), 4)
    insert_left_child(get_right_child(my_tree), 5)
    insert_right_child(get_right_child(my_tree), 6)
    print(my_tree)

make_tree()

#Oppgave 3
class Graph:
    graph = dict()
    searched = []

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)

    def print_graph(self):
        print(self.graph)

    def breadth_first_search(self, node):

        searched = [node]
        search_queue = [node]

        while search_queue:
            node = search_queue.pop(0)

            print('[', node, end=' ], ')

            if node in self.graph:
                for neighbour in self.graph[node]:
                    if neighbour not in searched:
                        searched.append(neighbour)
                        search_queue.append(neighbour)

    def depth_first_search(self, node):
        if node not in self.searched:
            print('[', node, end=' ], ')

            self.searched.append(node)
            if node in self.graph:
                for neighbour in self.graph[node]:
                    self.depth_first_search(neighbour)

mg = Graph()

def build_my_graph2():
    mg.add_edge('a', 'b')
    mg.add_edge('a', 'c')
    mg.add_edge('b', 'c')
    mg.add_edge('b', 'd')
    mg.add_edge('c', 'e')
    mg.add_edge('d', 'e')
    mg.add_edge('e', 'f')
    mg.add_edge('f', 'c')
    mg.add_edge('d', 'g')
    mg.add_edge('d', 'h')
    mg.depth_first_search('a')
    print('')

print('The printed output of the DFS algorithm is:', end=' ')
build_my_graph2()

#Oppgave 4

class BinarySearchTree:

    def __init__(self, value=None):
        self.value = value
        if self.value:
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        else:
            self.left_child = None
            self.right_child = None

    def is_empty(self):
        return self.value is None

    def insert(self, value):
        if self.is_empty():
            self.value = value
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()

        elif value < self.value:
            self.left_child.insert(value)

        elif value > self.value:
            self.right_child.insert(value)

    def compute_sum(self):
        if self.is_empty():
            return 0
        else:
            return self.left_child.compute_sum() + self.value + self.right_child.compute_sum()

    def compute_count(self):
        if self.is_empty():
            return []
        else:
            return (self.left_child.compute_count() + [(self.value)] + self.right_child.compute_count())







my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(8)
my_tree.insert(10)
print('sum:', my_tree.compute_sum())
print('number of nodes:', len(my_tree.compute_count()))