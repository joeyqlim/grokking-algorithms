# B: shortest weight is 60
# init graph
graph = {}
graph["start"] = {} # init start node
graph["start"]["a"] = 10 # edge from start to a, cost of 6
graph["a"] = {}
graph["a"]["b"] = 20
graph["b"] = {}
graph["b"]["fin"] = 30
graph["b"]["c"] = 1
graph["c"] = {}
graph["c"]["a"] = 1
graph["fin"] = {}

# init costs table
# tracks the lowest cost to reach each node
# if unknown, use infinity
infinity = float("inf") # infinity in python
costs = {}
costs["a"] = 10
costs["b"] = infinity
costs["c"] = infinity
costs ["fin"] = infinity

# init parents table
# used to find the final route backwards
parents = {}
parents["a"] = "start"
parents["b"] = None
parents["c"] = None
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
