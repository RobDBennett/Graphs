
def earliest_ancestor(ancestors, starting_node):
    parent_child = {}  # Create a dictionary. This will act as the graph.
    for rel in ancestors:  # Run through each ancestor pairing
        parent = rel[0]  # The first value is always the parent
        child = rel[1]  # The second value is always the child.
        if child not in parent_child:  # Check if the child exists in dict.
            # If not, set an empty set for parents.
            parent_child[child] = set()
        # Otherwise add the parents to the value set.
        parent_child[child].add(parent)
    # The above was taken from the add_edge/add_vertex of our graph class.

    earliest = -1  # Set default as -1 to pass tests.
    stack = []  # Start an empty stack.
    stack.append(starting_node)  # Add starting node to stack.
    # As in previous examples, while something is in the stack...
    while len(stack) > 0:
        current = stack.pop()  # Take first element of stack as current node.
        if current in parent_child:  # Checks that the seach object is in dict.
            # Cycle through each parent of current node.
            for parent in parent_child[current]:
                # Set starting lowest id to any parent.
                parent_lowest_id = parent
                if parent < parent_lowest_id:  # Check if the other parent is lower id.
                    parent_lowest_id = parent  # Set lowest id to that parent.
                stack.append(parent)  # Add parent to the stack.
            earliest = parent_lowest_id  # Set the earliest to lowest.
    return earliest  # Return earliest.
