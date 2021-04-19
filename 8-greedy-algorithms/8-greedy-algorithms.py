# Problem: igure out the smallest set of stations you can play on to cover all 50 states
# Optimal solution O(2^n):
## List every possible subset of stations, pick the set with the smallest number of stations that cover all 50 states.
# Greedy solution O(n^2):
## Pick the station that covers the most uncovered states, repeat until all states are covered.

# Init set of states to cover
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# Init hash map of stations
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# Init set of final stations
final_stations = set()

# Find the best station (covers most uncovered states)
while states_needed: # Iterate until all states are covered
	best_station = None
	states_covered = set()
	for station, states in stations.items(): # station = kfive; states = {'ca', 'az'}
		covered = states_needed & states # set intersection
		if len(covered) > len(states_covered):
			best_station = station
			states_covered = covered
	states_needed -= states_covered
	final_stations.add(best_station) # add the best station from each iteration to final set

print(final_stations) # {'kfive', 'kthree', 'kone', 'ktwo'}