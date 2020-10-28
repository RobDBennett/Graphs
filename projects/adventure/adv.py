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
Attempt 1-
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

def dft_trial(visited, room, current_step):
    if visited == None: #The first time this runs.
        visited = set() #Create an empty set.

    if room.name not in visited: #Check if name is already in visited set.
        visited.add(room.name) #Add to visited set. (No print necessary)
        if current_step: #If a current step exists (checks for starting run)
            
            #This step is very importance, since we are only tracking the steps further in if the room hasn't been visited,
            #we need to have a method of tracking the steps for existing rooms.

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
#Attempt 2, this time with graphing.
"""
Coder notes- 
I tried to create the graph and alter it in place with the above code, but since I was never using the player traveral,
it led to some issues with setting up the current room and previous room within the graph value dictionary. 
Since the test tells us the number of total rooms that we have to visit, maybe a while loop would be more effective.
Also, if we are forcing the player to walk, I will have less issues with the object return from the get_room_in_direction.

This will operate similarly (I think). We will set up the graph, traversal_path, probably a back_track steps (I don't know 
how else to track that) and a visited set. We'll set the while loop to run while the visited set is less than the total rooms.
Then we'll structure it like a DFT. Check if the current room (which we can tie to the player who is created above) is in visited.
We add it to visited, and then we check for the exits. Making the graph is tricky, but a dictionary within a dictionary feels like 
the best approach, that way we can update the different room directions as we go.
I'm not sure the best approach for how to update the graph rooms other than to set a current and previous room to different pointers
and moving through the maze.
If we update the graph for each room's direction to the proper room on that side, and the room we just left as the other, I think this
will work out.
Update- 
Using traversal_path as the back_track list failed pretty hard. Add back_track list.
"""

traversal_path = []
back_steps = {'w': 'e', 'e': 'w', 'n': 's', 's': 'n'}
graph = {}
back_track = []
visited = set()


def use_the_player():
    while len(visited) != len(room_graph): #Run till all rooms are visited.
        current_room = player.current_room.id #Set the current room to the players current_room
        if current_room not in visited: #Check if this room is in visited, like all DFT/S
            possible_exits = player.current_room.get_exits() #Find all exits
            exits = {} #Build a temporary dictionary for the exits.
            for exit in possible_exits: #Run through all possible exits.
                exits[exit] = "?" #Add a ? as the value to the exit's key.
            graph[current_room] = exits #Add the temp dictionary to the real one at the room id.
            visited.add(current_room) #Add the room to the visited
        if back_track: #Won't run the first time since there are no steps.
            #This will set the current room's graph so that the previous room is pointed to the last
            #step we took.
            graph[current_room][back_track[-1]] = previous_room #The first time this runs, there isn't a previous. 
        unchecked_direction = [] #Generate a temporary list.
        for key, value in graph[current_room].items(): #Collect all exits from  current room.
            if value == "?": #See if we've updated that direction yet
                unchecked_direction.append(key) #If not, add that direction to the temp list.
        if unchecked_direction: #Check if something is in the temp list.
            direction = unchecked_direction.pop() #Pull the last element from that list.
            previous_room = player.current_room.id #Set a previous_room to current room.
            player.travel(direction) #Move the player in that direction.
            next_room = player.current_room.id #Set the 'next_room' to the room the player is *now* in.
            graph[previous_room][direction] = next_room #Update graph at the previous room with the id for this one.
            traversal_path.append(direction) #Add movement to traversal_path for grading.
            back_track.append(back_steps[direction]) #Add the opposite movement to the back_track list
        else: #If there aren't any unchecked directions...
            opposite_direction = back_track.pop()  #Set up the backwards step.
            previous_room = player.current_room.id #Set the previous room to current.
            player.travel(opposite_direction) #Move the backwards step.
            next_room = player.current_room.id #Sets next room to the room you just stepped into.
            graph[previous_room][opposite_direction] = next_room #Updates graph for the backwards step.
            traversal_path.append(opposite_direction) #Adds step to traversal path.

use_the_player()

# This visits every room in 998 moves (again), uses the player traversal and generates the graph.

#Uncomment to see the generated graph.
#print(graph)

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
