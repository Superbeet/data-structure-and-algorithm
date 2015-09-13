# Chapter 4 - 4.2

# Given a directed graph, design an algorithm to find out 
# whether there is a route between two nodes.

#

def getNodes(node):
	print "get all nodes"
	return node_list

def getAdjacents(node):
	print "get adjacents"
	return node_list

# State_Candidates = {"Unvisited":1, "Visited":2, "Visiting":3}

def search(graph, start, end):

	if start is end:

		return True 

	for node in getNodes(graph):

		node.state = "Unvisited"

	queue = []

	queue.append(start)

	while not queue.isEmpty():

		node = queue.pop()
		
		if node is not None:

			for next_node in getAdjacents(node):

				if next_node.state is "Unvisited":

					if next_node is end:

						return True

				else:

					next_node.state = "Visited"

					queue.append(next_node)

			next_node.state = "Visiting"

	return False






