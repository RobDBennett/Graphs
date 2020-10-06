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
        q = Queue()  # Breadth-first is a Queue. Could also just have a list here, with append and pop(0)
        # Sets won't save duplicates, but also won't save order. Could be problematic later.
        visited = set()
        q.enqueue(starting_vertex)  # Adds starting node to tail of list.
        while q.size() > 0:
            v = q.dequeue()  # Removes item from the end of the list.
            if v not in visited:  # Checks if the item is in the set.
                print(v)  # Print to pass test.
                visited.add(v)  # Add to set.
                for neighbor in self.get_neighbors(v):  # Poor-man's recursion.
                    # Add each neighbor to the end of the queue.
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        q = Stack()  # Depth first is a Stack. Could also do this with a list with append and pop().
        # Sets won't save duplicates but also won't save order. Might be problematic later.
        visited = set()
        q.push(starting_vertex)  # Add starting node to the stack.
        while q.size() > 0:
            v = q.pop()  # Removes last item in the stack
            if v not in visited:  # Checks if removed item is in the set.
                # Prints if not. Mostly to pass tests. Could append this to a new list if we wanted.
                print(v)
                visited.add(v)  # Add to set.
                for neighbor in self.get_neighbors(v):  # Poor man's recursion.
                    q.push(neighbor)  # Add each neighbor to the stack.

    # Add some items that need to be passed in.
    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        First time this is run, will automatically generate empty Stack and set.
        """
        if visited == None:
            visited = set()

        if starting_vertex not in visited:  # Checks if this item is in the visited set.
            print(starting_vertex)  # Print to pass test.
            visited.add(starting_vertex)  # Adds item to set.
            # Find all of the neighbors for this point.
            for neighbor in self.get_neighbors(starting_vertex):
                # Run recursion on all of the neighbors.
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        path = Queue()  # Start up an empty Queue.
        # Add path to queue. Note that its a list.
        path.enqueue([starting_vertex])
        visited = set()  # Start visited set.
        while path.size() > 0:  # Continues until path dries up.
            # Remove head of the path and cast to variable. This is a list.
            new_path = path.dequeue()
            new_vertex = new_path[-1]  # Check last item in the variable (list)
            if new_vertex not in visited:  # If last item isn't in visited
                if new_vertex is destination_vertex:  # Checks if that last item is the destination.
                    return new_path  # Return the dequeue list.
                # Otherwise add that item to the visited set.
                visited.add(new_vertex)
                # For all of the neighbors from this last point=
                for neighbor in self.get_neighbors(new_vertex):
                    # If you do not copy the original path, it errors.
                    #Another way would be path = new_path + neighbor
                    path_copy = new_path.copy()
                    # Add the neighbor to the end of the list (the list that was dequeued)
                    path_copy.append(neighbor)
                    # Add that new list to the end of the queue. Repeat above.
                    path.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()  # Start up an empty Stack.
        stack.push(starting_vertex)  # Add start point to stack.
        visited = set()  # Set an empty visited set.
        visited.add(starting_vertex)  # Add starting point to set.
        while stack.size() > 0:  # Continue while stack exists.
            # Set a pointer and remove the last item from stack.
            new_node = stack.pop()
            visited.add(new_node)  # Add that node to set.
            # Find all neighbors for that node.
            for neighbor in self.get_neighbors(new_node):
                if neighbor not in visited:  # Check if they are already in set.
                    stack.push(neighbor)  # If not, add to stack.
                if neighbor is destination_vertex:  # Check if neighbor is the destination point.
                    visited.add(neighbor)  # Add to set.
                    # Return set, but cast to a list to pass the test.
                    return list(visited)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        First time this runs, it will automatically create an empty set for visited items, and a blank list for the path.
        """
        visited.add(starting_vertex)  # Add starting point to visited set.
        path = path + [starting_vertex]  # Add starting point to path list.
        # Check if starting point is the destination.
        if starting_vertex == destination_vertex:
            # Return the path list (needs to be a list to pass test.)
            return path
        # Generates a list of all neighbors.
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:  # Checks if neighbor is already in visited set.
                # Performs recursion on each neighbor not already in the set.
                newpath = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path)
                if newpath is not None:  # Checks that recursion for content.
                    return newpath  # Returns those that have something.


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
