
def earliest_ancestor(ancestors, starting_node):
    for ancestor in ancestors:
        if ancestor[1] == starting_node:
            return ancestor[0]
        if ancestor[0] == starting_node:
            return earliest_ancestor(ancestors, ancestor)