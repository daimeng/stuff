# python3

# retrieve by bfs and edge counting
def get_order(g, stb):
	# resulting list
	li = []

	# get mutable edge counts structure from graph
	in_cnt = { k:len(v) for (k, v) in g['ins'].items() }

	# traversal queue (set has order)
	# push entry nodes of in count 0
	q = [ k for k in stb if k not in in_cnt ]
	visited = set(q)

	while q:
		node = q.pop()
		if node in g['outs']:
			# decrement all in counts
			# add to queue if node is now new entry
			for o in stb:
				if o in g['outs'][node]:
					in_cnt[o] -= 1
					# do not add node unless all 'in' dependencies resolved
					if in_cnt[o] == 0 and o not in visited:
						q.append(o)
						visited.add(o)
		li.append(node)

	return li

# builds graph as adjacency set, with mirror set
def build_graph(input):
	g = { 'ins': {}, 'outs': {} }
	for line in input:
		k, adjs = line[0], line[1:]
		s = g['outs'].get(k, set())
		g['outs'][k] = s | set(adjs)
		for adj in adjs:
			s = g['ins'].get(adj, set())
			g['ins'][adj] = s | set(k)

	return g
