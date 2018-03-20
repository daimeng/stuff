import unittest
from bfs_dep_order import build_graph, get_order

class BfsDepOrderTest(unittest.TestCase):
	def test_build(self):
		input = [
	    	['A', 'B', 'C'],
			['B', 'C', 'D'],
    	  	['C', 'D']
		]
		g = build_graph(input)
		self.assertEqual(g,
			{	'ins': {
					'B': {'A'},
					'C': {'B', 'A'},
					'D': {'C', 'B'}
				},
				'outs': {
					'A': {'C', 'B'},
					'B': {'C', 'D'},
					'C': {'D'}
				}
			}
		)

	def test(self):
		input = [
			['A', 'B', 'C'],
			['B', 'C', 'D'],
			['C', 'D']
		]

		g = build_graph(input)
		self.assertEqual(
			get_order(g, ['A', 'B', 'C', 'D']),
			['A', 'B', 'C', 'D']
		)

	def test2(self):
		input = [
			['A', 'D', 'E', 'C', 'B'],
			['B', 'C', 'E'],
			['D', 'E']
		]

		# breadth iterations, left to right
		# 1:  +A
		# 2: +D +B
		# 3: +E +C

		g = build_graph(input)
		self.assertEqual(
			get_order(g, ['A', 'B', 'C', 'D', 'E']),
			['A', 'D', 'B', 'E', 'C']
		)

	def test_fullcycle(self):
		input = [
			['A', 'B'],
			['B', 'C'],
			['C', 'A'],
		]

		# will not be able to find entry, resulting in empty list
		g = build_graph(input)
		self.assertEqual(
			get_order(g, ['A', 'B', 'C']),
			[]
		)

	def test_cycle(self):
		input = [
			['A', 'B'],
			['B', 'C'],
			['C', 'D'],
			['D', 'B']
		]

		# will not be able to find next entry after first iteration
		g = build_graph(input)
		# test if input nodes length is same as result to determine if there is cycle
		self.assertEqual(
			get_order(g, ['A', 'B', 'C', 'D']),
			['A']
		)

if __name__ == '__main__':
	unittest.main()