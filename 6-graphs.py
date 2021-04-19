from collections import deque # python library has a queue function

# create graph
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def is_seller(person):
	return person[-1] == "m"

def search(name):
	# initialize queue
	search_queue = deque()
	search_queue += graph[name]

	# keep track of people already searched
	searched = []

	# BFS
	while search_queue:
		person = search_queue.popleft() # (pop first item i.e. JS shift)
		if not person in searched:
			if is_seller(person):
				print (person + " is a mango seller!")
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	return False

search("you")