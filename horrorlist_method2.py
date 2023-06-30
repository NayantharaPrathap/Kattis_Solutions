from collections import deque

# Create a graph class (data structure)
class Graph(object):

    # Initialize our data members (equal to a constructor in OOP)
    # Quick explanation of self; refers to instance of which it is called
    def __init__(self, nodes, costIndex, rootNodes):
        # Adjacency list data structure: 
        # (ex: {0:[1, 2, 3],
        #       1:[0, 4, 5],
        #       2:[0, 4, 5],
        #       node:[neighbor1, n2, n3, ...]
        #       })
        self.graph = {node: [] for node in range(nodes)}

        # Queue data structure (FIFO)
        self.queue = deque()

        # Set listing all possible nodes: set of n
        # ex: {0, 1, 2, 3 ... n}
        self.notVisited = {n for n in range(nodes)}

        # In this context, the horrorIndex
        self.costIndex = costIndex

        # In this context, the horrorList
        self.rootNodes = rootNodes
    
    # Function to add a relationship (a.k.a edge) to a graph (node -> neighbor)
    def addEdge(self, node, neigbor):
        # Add the neighbor into the adjacency list of the node
        self.graph[node].append(neigbor)

        # Add the node into the adjacency list of the neighbor
        self.graph[neighbor].append(node)
    
    # Our friend, the BFS!
    def breadthFirstSearch(self):
        
        # Initialize arbitrary highestCost and highestNode variables
        # Used to track the highest indexed movie and the cost of that movie
        highestCost, highestNode = -1, -1

        # BFS; while our queue is not empty (truthy value)
        while self.queue:
            # Set node var to dequeued value (our current node)
            node = self.queue.popleft()

            # Set cost to node's cost from our costIndex (our current cost)
            cost = self.costIndex[node]

            # If the cost is greater that our highestCost var
            # or if the cost is equal, and the node is less than the highestNode
            # So if the cost is higher; the index is higher (we want that as our answer!)
            # We check only if the node < highestNode because we want to make 
            # sure we're only returning the min node with the same cost
            if cost > highestCost or (cost == highestCost and node < highestNode):

                # Our most current dequeued node cost becomes the highest cost
                # Our most current dequeued node becomes the highest node
                highestCost, highestNode = cost, node

            # BFS; for neighbor in the adjacency list of the current node
            for neighbor in self.graph[node]:

                # If the neighbor has not already been visited
                if neighbor in self.notVisited:

                    # Remove from the notVisited Set
                    self.notVisited.remove(neighbor)

                    # Append the neigbor node into the queue
                    self.queue.append(neighbor)

                    # Set the cost of the neighbor to the current cost + 1
                    self.costIndex[neighbor] = cost + 1

        # Once there's nothing left in the queue; return the highestNode
        return highestNode
    
    def findHighestIndex(self):
        # Set up our rootNodes in the queue and remove them from our notVisited
        for root in self.rootNodes:
            self.notVisited.remove(root)
            self.queue.append(root)
        
        # Find the highestNode from doing a breadthFirstSearch from each rootNode
        highestNode = self.breadthFirstSearch()

        # If the notVisited set is empty (therefore every node was visited)
        # The highestNode has the highest horror index (or highest cost)
        if not self.notVisited:
            return highestNode
        else:
            # If the notVisited set is not empty (therefore every node has not been visited)
            # Find the min node in the notVisited set
            return min(self.notVisited)


# This is where our code starts!
# Declare and initialize the n, h, and l values from input as int
n, h, l = [int(x) for x in input().split()]

# Create a set of horror movies from input as int
horrorList = {int(i) for i in input().split()}

# Create the horror index; use ternary operator to set key value
# k: None if k is not in horror list else k: 0
# Movies in the horrorList have a known value, all other movies have no known value
horrorIndex = {k: None if k not in horrorList else 0 for k in range(n)}

# Create an instance of our graph class with 
# n = nodes, horrorIndex = costIndex, and horrorList = rootNodes
movieGraph = Graph(n, horrorIndex, horrorList)

# For relationship (empty var cause not used) in range of number of relationships
for _ in range(l):
    # Declare and initialize node and neighbor from input as int
    node, neighbor = [int(x) for x in input().split()]

    # Add an edge to our graph (adjacency list data structure)
    movieGraph.addEdge(node, neighbor)

# Call our findHighestIndex to find the 
# node with the highest index value (highest cost)
print(movieGraph.findHighestIndex())
#print(horrorIndex)
