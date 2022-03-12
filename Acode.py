class Node():
    #@source based off of https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
    """A node class for A* Pathfinding"""

    #A* is an algorithm for finding the shortest path towards a set goal

  
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
    
    #Equals method tests for position
    def __eq__(self, other):
        return self.position == other.position

    #Used for debug: str() gives position as ordered pair
    def __str__(self):
        return str(self.position)

    #Comparisons: uses f-value (how optimal of a choice this point is)
    def __lt__(self, other):
        return self.f > other.f

    def __gt__(self, other):
        return self.f < other.f

def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both unvisited points list and wall/visited points list
    open_list = []
    closed_list = []

    # Add all obstacles to closed list
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if maze[i][j] == 1:
                closed_list.append(Node(None, (i, j)))
  
    # Add the start node
    open_list.append(start_node)
      
    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        open_list.sort()
        current_node = open_list[-1]
        current_index = -1

        # Pop current off open list, add to closed list
        current_node = open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal; return shortest path
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Returns reversed path

        # Generate children of current node
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0],
                             current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (
                    len(maze) -
                    1) or node_position[0] < 0 or node_position[1] > (
                        len(maze[0]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append to found children
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if child in closed_list:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0])**2) + (
                (child.position[1] - end_node.position[1])**2)
            child.f = child.g + child.h

            # Child is already in the open list
            if child in open_list:
                if child.f < open_list[open_list.index(child)].f:
                    # Checks for lower f value
                    open_list[open_list.index(child)] = child
                else:
                    continue
            else:

            # Add the child to the open list
                open_list.append(child)