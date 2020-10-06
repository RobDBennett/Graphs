#Start of class. Basic run down of graphs.
#Start with a LinkedList. Or a tree. LL are a graph, but graphs have odd rules, and they can have multiple connections between nodes.
# They can also have loops, or connection points. Connects -> Edges -> Weights.
#If an Edge is directed, that means that its one way. Undirected Edge makes two way directions. (typically represented by a line without arrowheads)
# If there are only undirected edges, we call it an undirected graph. If none of the edges have any weights on them, it is an unweighted graph.

#We can tranverse a cyclic graph by tracking which nodes we have visited. If a graph has any cycles in it, its a cyclic graph. Otherwise its acyclic. 

#Representing graphs:"
# Adjacency matrix: 
#big grid that has true/false values showing which nodes are adjacent or edge weights

#Adjacency lists:
# A: [B, D] -> Or as a dictionary instead of a list.
# B: [D, C]
# C: [C, B]
# D: []

#Graph classes with edges and vertex (nodes)

class Queue: #Add stuff. From CS unit 1.
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v_from, v_to):
        if v_from in self.vertices and v_to in self.vertices:

            self.vertices[v_from].add(v_to)
        else:
            raise IndexError("Nonexistent vertex")

    def is_connected(self, v_from, v_to):
        if v_from in self.vertices and v_to in self.vertices:
            return v_to in self.vertices[v_from]
        else:
            raise IndexError("Nonexistent vertex")

    def get_neighbors(self, v):
        return self.vertices[v]

    def bft(self, starting_vertex_id):
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex_id)
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex_id):
        q = Stack()
        visited = set()
        q.push(starting_vertex_id)
        while q.size() > 0:
            v = q.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    q.push(neighbor)



#Breadth first tranversing.
#Init- Add the start vert to the queue.
#While queue is not empty:
#pop current vert off queue.
#If not visited
#'visit' the node
#track it as visited
#Add all neighbors (adjacent nodes)

#Depth first tranversing.
#Init- add the starting vert to the stack

#Word changing. Given a dictionary, and then a list of two words. Changing
# one letter at a time, transform the first word to the end word, return shortest path.
words = set()
text = open('words.txt', 'r')
for word in text:
    word= word.strip()
    words.add(word)


def get_neighbors(word):
    neighbors = []
    for w in words:
        if len(w) == len(word):
            diff_count = 0
            for i in range(len(w)):
                if w[i] != word[i]:
                    diff_count +=1
                if diff_count > 1:
                    break
            if diff_count == 1:
                neighbors.append(w)
    return neighbors

def bfs(begin_word, end_word):
    visited = set()
    q = Queue()
    q.enqueue([begin_word])
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            visited.add(v)
            if v == end_word:
                return path
            for neighbor in get_neighbors(v):
                path_copy = path + [neighbor]
                q.enqueue(path_copy)

print(bfs('smash', 'kills'))


#string.ascii_lowercase
#list(string.ascii_lowercase)

import string

def get_neighbors(word):
    neighbors = []
    letters = list(string.ascii_letters)
    word_letters = list(word)
    for i in range(len(word_letters)):
        for l in letters:
            word_letter_copy = list(word_letters)
            word_letter_copy[i] = l
            candidate_word = "".join(word_letter_copy)
            if candidate_word != word and candidate_word in words:
                neighbors.append(candidate_word)
    return neighbors