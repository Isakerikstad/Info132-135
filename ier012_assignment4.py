#Assignment 4 INFO 135

#Oppgave 1

#Set b) represents the correct Edge set of the graph.

def examine(partial_sol):
    for i in range(len(partial_sol)):
        for j in range(i + 1, len(partial_sol)):
            if attacks(partial_sol[i], partial_sol[j]):
                return ABANDON
    if len(partial_sol) == NUM_QUEENS:
        return ACCEPT
    else:
        return CONTINUE

def extend(partial_sol):
    results = []
    row = len(partial_sol) + 1
    for column in COLUMNS:
        new_solution = list(partial_sol)
        new_solution.append(column + str(row))
        results.append(new_solution)
    return results

def attacks(p1, p2):
    column1 = COLUMNS.index(p1[0]) + 1
    row1 = int(p1[1])
    column2 = COLUMNS.index(p2[0]) + 1
    row2 = int(p2[1])
    return row1 == row2 or column1 == column2 or abs(row1 - row2) == abs(column1 - column2)

list_of_solutions = []
def solve(partial_sol):
    global list_of_solutions
    exam = examine(partial_sol)
    if exam == ACCEPT:
        print(partial_sol)
        list_of_solutions.append(partial_sol)
    elif exam != ABANDON:
        for p in extend(partial_sol):
            solve(p)

def is_solution(candidate_solution):
    for a in candidate_solution:
        for b in candidate_solution:
            if a == b:
                pass
            elif attacks(a, b) is True:
                return 'Invalid'
    return 'Valid'

COLUMNS = "abcde"
NUM_QUEENS = len(COLUMNS)
ACCEPT = 1
CONTINUE = 2
ABANDON = 3
all_solutions = []

solve([])


candidate_solution1 = list_of_solutions[0]
candidate_solution2 = ['e4', 'a1', 'c5', 'd2', 'b1']
candidate_solution3 = list_of_solutions[2]
candidate_solution4 = list_of_solutions[3]
candidate_solution5 = list_of_solutions[4]


result1 = is_solution(list_of_solutions[0])
result2 = is_solution(candidate_solution2)
result3 = is_solution(list_of_solutions[2])
result4 = is_solution(list_of_solutions[3])
result5 = is_solution(list_of_solutions[4])


print("Candidate Solution 1:", result1)
print("Candidate Solution 2:", result2)
print("Candidate Solution 3:", result3)
print("Candidate Solution 4:", result4)
print("Candidate Solution 5:", result5)

#oppgave 3
class Graph:
    graph = dict()


    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)


    def find_cycle(self, node):
        searched = [node]
        search_queue = [node]

        while search_queue:
            node = search_queue.pop(0)

            if node in self.graph:
                for neighbour in self.graph[node]:
                    if neighbour not in searched:
                        searched.append(neighbour)
                        search_queue.append(neighbour)
                    elif neighbour in searched:
                        return 'Cycle found'
        return 'Cycle not found'

my_graph = Graph()
my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'B')
my_graph.add_edge('C', 'J')
my_graph.add_edge('D', 'E')
my_graph.add_edge('D', 'F')
my_graph.add_edge('E', 'C')
my_graph.add_edge('E', 'G')
my_graph.add_edge('F', 'H')
my_graph.add_edge('G', 'I')

result = my_graph.find_cycle('D')
print(result)
