# tests/test_bst.py

import unittest
from b_search_tree.bst import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        # Inizializza un albero binario di ricerca vuoto
        self.bst = BinarySearchTree()

    def test_insert(self):
        # Inserisci alcune chiavi e verifica che siano presenti
        keys = [15, 10, 20, 8, 12, 17, 25]
        for key in keys:
            self.bst.insert(key)

        # Verifica che tutte le chiavi siano state inserite
        for key in keys:
            result = self.bst.search(key)
            self.assertIsNotNone(result, f"Chiave {key} non trovata nel BST")

    def test_search(self):
        # Inserisci alcune chiavi
        keys = [5, 15, 3, 12, 10]
        for key in keys:
            self.bst.insert(key)

        # Testa la ricerca di chiavi esistenti
        self.assertIsNotNone(self.bst.search(10), "Chiave 10 non trovata nel BST")
        self.assertIsNotNone(self.bst.search(5), "Chiave 5 non trovata nel BST")

        # Testa la ricerca di una chiave inesistente
        self.assertIsNone(self.bst.search(99), "Chiave 99 trovata erroneamente nel BST")


if __name__ == "__main__":
    unittest.main()
