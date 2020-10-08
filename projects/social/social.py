import math
import random


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        random.shuffle(possible_friendships)

        for i in range(0, math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
            #self.add_friendship(*friendship)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        This will be a Breadth-First Search function, modified to find all paths.
        """
        visited = {}  # Note that this is a dictionary, not a set
        queue = []  # Instantiate an empty queue
        queue.append([user_id])  # Add the starting id to the queue as a list.
        while queue:  # Continue while items exist in the queue.
            current_path = queue.pop(0)  # Find the first list in the queue.
            # Find the last item of that list.
            current_vertex = current_path[-1]
            # Check if last item exists in our friend dictionary.
            if current_vertex not in visited:
                # If not, add it with the value being the path from the starting node to it.
                visited[current_vertex] = current_path
                # Find all the friends of that node.
                for friend in self.friendships[current_vertex]:
                    if friend not in visited:  # Check if the friends are in the visited.
                        # If not, make a copy of the path to it.
                        new_path = current_path.copy()
                        # Add the current friend to that path.
                        new_path.append(friend)
                        # Add that path to the queue
                        queue.append(new_path)  
        return visited  # When the queue is exhausted, return the dictionary.

    


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
