# b_search_tree/bst.py

from .bst_node import BSTNode

class BinarySearchTree:
    def __init__(self):
        """
        Inizializza un albero binario di ricerca vuoto.
        """
        self.root = None
        # Contatori per misurare le performance
        self.nodes_read = 0
        self.nodes_written = 0

    def search(self, key, node=None):
        """
        Cerca una chiave nell'albero binario di ricerca.

        :param key: Chiave da cercare.
        :param node: Nodo da cui iniziare la ricerca (default è la radice).
        :return: Nodo con la chiave cercata o None se non esiste.
        """
        if node is None:
            node = self.root

        while node is not None:
            self.nodes_read += 1  # Incrementa il contatore dei nodi letti
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def insert(self, key):
        """
        Inserisce una chiave nell'albero binario di ricerca.

        :param key: Chiave da inserire.
        """
        new_node = BSTNode(key)
        self.nodes_written += 1  # Scriviamo un nuovo nodo
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        parent = None
        while current is not None:
            parent = current
            self.nodes_read += 1  # Leggiamo il nodo corrente
            if key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

