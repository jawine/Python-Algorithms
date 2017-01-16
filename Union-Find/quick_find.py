#!/usr/bin/python3
"""
Track connectedness of multiple subsets of a set (dynamic connectivity/disjoint set problem)

The union command will, worst case, perform in O(n**2) (quadratic) time. It may not perform well with a large input N,
as it will take N**2 list accesses to process a sequence of up to N union commands on up to N objects.

We can test the execution time of union operations and connected queries using the timeit module.
It is clear that as N becomes large, this implementation of union does not scale. The connected
query performs in relatively constant time since it is merely comparing based on indexes of the list
"""

import unittest


class QuickFind:
    """Initialize a list of given size, indexes of the list represent nodes,
    while the list values identify the set to which they belong. Each node begins
    pointing to itself (id[i] == i)"""
    def __init__(self, size):
        self.id = [i for i in range(size)]

    """Set the identifier for the set to which p belongs equal to the identifier of q,
    forming a connection between the two sets"""
    def union(self, p, q):
        p_id = self.id[p]
        q_id = self.id[q]
        id_length = len(self.id)
        for node in range(id_length):
            if self.id[node] is p_id:
                self.id[node] = q_id

    """Return True if the set identifier of p equals the set identifier of q, False if they are in different sets"""
    def connected(self, p, q):
        return self.id[p] == self.id[q]

class QuickFindTest(unittest.TestCase):

    def setUp(self):
        self.quick_find_test = QuickFind(100)

        self.quick_find_test.union(2, 88)
        self.quick_find_test.union(4, 42)
        self.quick_find_test.union(24, 96)
        self.quick_find_test.union(4, 24)
        self.quick_find_test.union(88, 4)

    def test_connected(self):
        self.assertTrue(self.quick_find_test.connected(2, 88))
        self.assertTrue(self.quick_find_test.connected(2, 42))
        self.assertTrue(self.quick_find_test.connected(4, 96))

if __name__ == "__main__":
    unittest.main()