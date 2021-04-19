# A: shortest weight is 8
# init graph
graph = {}
graph["start"] = {} # init start node
graph["start"]["a"] = 5 # edge from start to a, cost of 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["d"] = 4
graph["a"]["c"] = 2
graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["c"] = 7
graph["c"] = {}
graph["c"]["fin"] = 1
graph["d"] = {}
graph["d"]["c"] = 6
graph["d"]["fin"] = 3
graph["fin"] = {}

# init costs table
# tracks the lowest cost to reach each node
# if unknown, use infinity
infinity = float("inf") # infinity in python
costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs ["fin"] = infinity

# init parents table
# used to find the final route backwards
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["fin"] = None

# init array to keep track of processed nodes
processed = []

# function to find lowest cost node
def find_lowest_cost_node(costs):
	lowest_cost = float("inf")
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node

# Djikstra's Algorithm
node = find_lowest_cost_node(costs) # find the lowest cost node not in processed --> b
while node is not None: # while there is a remaining node to be processed
	cost = costs[node]
	neighbours = graph[node]
	for n in neighbours.keys():
		new_cost = cost + neighbours[n]
		if costs[n] > new_cost: # if existing cost of getting to fin > new cost
			costs[n] = new_cost # replace new cost
			parents[n] = node # update parent node
	processed.append(node) # add node to processed list
	node = find_lowest_cost_node(costs) # find the next lowest cost node

print (costs["fin"])
