"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Nonexistent vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue() #Breadth-first is a Queue. Could also just have a list here, with append and pop(0)
        visited = set() #Sets won't save duplicates, but also won't save order. Could be problematic later.
        q.enqueue(starting_vertex) #Adds starting node to tail of list.
        while q.size() > 0: 
            v = q.dequeue() #Removes item from the end of the list.
            if v not in visited: #Checks if the item is in the set.
                print(v) #Print to pass test.
                visited.add(v) #Add to set.
                for neighbor in self.get_neighbors(v): #Poor-man's recursion. 
                    q.enqueue(neighbor) #Add each neighbor to the end of the queue.

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        q = Stack() #Depth first is a Stack. Could also do this with a list with append and pop().
        visited = set() #Sets won't save duplicates but also won't save order. Might be problematic later.
        q.push(starting_vertex) #Add starting node to the stack.
        while q.size() > 0:
            v = q.pop() #Removes last item in the stack
            if v not in visited: #Checks if removed item is in the set.
                print(v) #Prints if not. Mostly to pass tests. Could append this to a new list if we wanted.
                visited.add(v) #Add to set.
                for neighbor in self.get_neighbors(v): #Poor man's recursion.
                    q.push(neighbor) #Add each neighbor to the stack.

    def dft_recursive(self, starting_vertex, stack=Stack(), visited=set()): #Add some items that need to be passed in.
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        First time this is run, will automatically generate empty Stack and set.
        """
        if starting_vertex not in visited: #Checks if this item is in the visited set.
            print(starting_vertex) #Print to pass test.
            visited.add(starting_vertex) #Adds item to set.
            for neighbor in self.get_neighbors(starting_vertex): #Find all of the neighbors for this point.
                self.dft_recursive(neighbor, stack, visited) #Run recursion on all of the neighbors.
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        path = Queue() #Start up an empty Queue.
        path.enqueue([starting_vertex]) #Add path to queue. Note that its a list.
        visited = set() #Start visited set.
        while path.size() > 0: #Continues until path dries up.
            new_path = path.dequeue() #Remove head of the path and cast to variable. This is a list.
            edge = new_path[-1] #Check last item in the variable (list)
            if edge not in visited: #If last item isn't in visited
                if edge is destination_vertex: #Checks if that last item is the destination.
                    return new_path #Return the dequeue list.
                visited.add(edge) #Otherwise add that item to the visited set.
                for neighbor in self.get_neighbors(edge): #For all of the neighbors from this last point=
                    path_copy = new_path.copy() #This fixed an error in the code. Not sure why.
                    path_copy.append(neighbor) #Add the neighbor to the end of the list (the list that was dequeued)
                    path.enqueue(path_copy) #Add that new list to the end of the queue. Repeat above.


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack() #Start up an empty Stack.
        stack.push(starting_vertex) #Add start point to stack.
        visited = set() #Set an empty visited set.
        visited.add(starting_vertex) #Add starting point to set.
        while stack.size() > 0: #Continue while stack exists.
            new_node = stack.pop() #Set a pointer and remove the last item from stack.
            visited.add(new_node) #Add that node to set.
            for neighbor in self.get_neighbors(new_node): #Find all neighbors for that node.
                if neighbor not in visited: #Check if they are already in set.
                    stack.push(neighbor) #If not, add to stack.
                if neighbor is destination_vertex: #Check if neighbor is the destination point.
                    visited.add(neighbor) #Add to set.
                    return list(visited) #Return set, but cast to a list to pass the test.
        

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        First time this runs, it will automatically create an empty set for visited items, and a blank list for the path.
        """
        visited.add(starting_vertex) #Add starting point to visited set.
        path = path + [starting_vertex] #Add starting point to path list.
        if starting_vertex == destination_vertex: #Check if starting point is the destination.
            return path #Return the path list (needs to be a list to pass test.)
        for neighbor in self.get_neighbors(starting_vertex): #Generates a list of all neighbors.
            if neighbor not in visited: #Checks if neighbor is already in visited set.
                newpath = self.dfs_recursive(neighbor, destination_vertex, visited, path) #Performs recursion on each neighbor not already in the list.
                if newpath is not None: #Checks that recursion for content.
                    return newpath  #Returns those that have something.

        # Infinite recusions. Try another way.
        # if stack == None and visited == None:
        #     stack = Stack()
        #     visited = set()
        # stack.push(starting_vertex)
        # visited.add(starting_vertex)
        # if stack.size() > 0:
        #     new_node = stack.pop()
        #     for neighbor in self.get_neighbors(new_node):
        #         if new_node not in visited:
        #             print(new_node)
        #             visited.add(new_node)
        #         if neighbor is destination_vertex:
        #             visited.add(neighbor)
        #             return list(visited)
        #         self.dfs_recursive(neighbor, destination_vertex, visited, stack)
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
