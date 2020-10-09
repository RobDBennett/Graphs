from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
"""
Coding notes-
I'm not sure if a depth first or breadth first is fewer steps. My poking around the internet
tells me that depth first is generally prefered when you have to traverse the entire graph, so that 
will be my first attempt.
My favorite code that I wrote on day 1 was recursive, so I will be trying that first, since run time isn't
an issue. 
The DFT_Recursive function that we wrote required a starting_vertex (starting room) and a visited set.
However, since we need to measure what steps we will take, we will also need to figure out a way to backtrack
easily if we stumble upon a dead end. We will also need a way to track our total path.
For the function, I think we'll need a visited set(), current_vertex(room), total traversal_path, and
whatever our current step is. We need to create the set within the function to avoid python errors. Also
the first time we run this, the current step will be nothing since we haven't moved yet.

For the actual function, we will create the set if it doesn't exist. Then we will need to
add the room.name to that set if its not already present. We will need to add our step to traversal_path
if it exists.
Then we will need to run the get_neighbors (get_exits()). The rooms also has a function to check if there is
room in a given direction that we can use to check the name of that room without going there. If its not 
a room that we have visited yet, then we will want to recursive ourselves into that room. And we'll probably want
to add something to the traversal_path.
"""

traversal_path = []
back_steps = {'w': 'e', 'e': 'w', 'n': 's', 's': 'n'}
graph = {}


def dft_trial(visited, room, current_step):
    if visited == None:  # The first time this runs.
        visited = set()  # Create an empty set.

    if room.name not in visited:  # Check if name is already in visited set.
        visited.add(room.name)  # Add to visited set. (No print necessary)
        exits = {}
        possible_exits = room.get_exits()
        for exit in possible_exits:
            exits[exit] = "?"
        graph[room.name] = exits
        if current_step:  # If a current step exists (checks for starting run)
            """
            This step is very importance, since we are only tracking the steps further in if the room hasn't been visited,
            we need to have a method of tracking the steps for existing rooms.
            """
            traversal_path.append(
                current_step)  # Add the current step to the traversal map.
        for exit in room.get_exits():  # Get all exits from the current room
            # Use the room function rather than player for consistency. Cast a variable with the movement
            # action to the next room
            room_in_direction = room.get_room_in_direction(exit)
            if room_in_direction.name not in visited:  # Check if next room is in visited
                # If not, recurse onto that room.
                dft_trial(visited, room_in_direction, exit)
                # Add to traversal path
                traversal_path.append(back_steps[exit])


dft_trial(visited=None, room=player.current_room, current_step="")
# This visits every room in 998 moves. I don't feel super great about it, though. I feel like its not
# properly tracking when we have to back up.
print(graph)


"""
def dft_trial(visited, room, current_step):
    if visited == None: #The first time this runs.
        visited = set() #Create an empty set.

    if room.name not in visited: #Check if name is already in visited set.
        visited.add(room.name) #Add to visited set. (No print necessary)
        if current_step: #If a current step exists (checks for starting run)
            """
#This step is very importance, since we are only tracking the steps further in if the room hasn't been visited,
#we need to have a method of tracking the steps for existing rooms.
"""
            traversal_path.append(current_step) #Add the current step to the traversal map.
        for exit in room.get_exits(): #Get all exits from the current room
            #Use the room function rather than player for consistency. Cast a variable with the movement
            #action to the next room
            room_in_direction = room.get_room_in_direction(exit) 
            if room_in_direction.name not in visited: #Check if next room is in visited
                dft_trial(visited, room_in_direction, exit) #If not, recurse onto that room.
                traversal_path.append(back_steps[exit]) #Add to traversal path

dft_trial(visited= None, room=player.current_room, current_step="")
#This visits every room in 998 moves. I don't feel super great about it, though. I feel like its not
#properly tracking when we have to back up.
print(graph)
"""

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
