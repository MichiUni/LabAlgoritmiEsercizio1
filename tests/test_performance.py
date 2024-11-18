# tests/test_performance.py

import unittest
from btree.b_tree import BTree
from binary_search_tree.bst import BinarySearchTree

class TestPerformance(unittest.TestCase):

    def test_performance(self):
        # Dataset di test
        keys = list(range(1, 1001))  # Inseriamo 1000 chiavi
        b_tree = BTree(t=5)
        bst = BinarySearchTree()

        # Inserimento nel B-tree
        for key in keys:
            b_tree.insert(key)

        # Inserimento nel BST
        for key in keys:
            bst.insert(key)

        # Misura i nodi letti/scritti per ciascuna struttura
        print("B-Tree: Nodi letti:", b_tree.nodes_read, ", Nodi scritti:", b_tree.nodes_written)
        print("BST: Nodi letti:", bst.nodes_read, ", Nodi scritti:", bst.nodes_written)

if __name__ == "__main__":
    unittest.main()
