class BSTNode:
    def __init__(self, key, parent=None):
        """
        Inizializza un nuovo nodo per l'albero binario di ricerca.

        :param key: Chiave del nodo.
        :param parent: Nodo genitore (opzionale).
        """
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent  # Opzionale, può essere utile per la cancellazione
