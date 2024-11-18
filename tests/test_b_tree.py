# tests/test_b_tree.py

import unittest
from btree.b_tree import BTree

class TestBTree(unittest.TestCase):

    def setUp(self):
        # Inizializza un B-albero con grado minimo 2 (per semplicità)
        self.b_tree = BTree(t=2)

    def test_insert(self):
        # Inserisci alcune chiavi e verifica che siano presenti
        keys = [10, 20, 5, 6, 12, 30, 7, 17]
        for key in keys:
            self.b_tree.insert(key)

        # Verifica che tutte le chiavi siano state inserite
        for key in keys:
            result = self.b_tree.search(key)
            self.assertIsNotNone(result, f"Chiave {key} non trovata nel B-albero")

    def test_search(self):
        # Inserisci alcune chiavi
        keys = [15, 8, 25, 3, 10]
        for key in keys:
            self.b_tree.insert(key)

        # Testa la ricerca di chiavi esistenti
        self.assertIsNotNone(self.b_tree.search(10), "Chiave 10 non trovata nel B-albero")
        self.assertIsNotNone(self.b_tree.search(25), "Chiave 25 non trovata nel B-albero")

        # Testa la ricerca di una chiave inesistente
        self.assertIsNone(self.b_tree.search(99), "Chiave 99 trovata erroneamente nel B-albero")


if __name__ == "__main__":
    unittest.main()
