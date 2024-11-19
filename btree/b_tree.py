from .b_tree_node import BTreeNode

class BTree:
    def __init__(self, t):
        """
        Inizializza un nuovo B-albero.

        :param t: Il grado minimo del B-albero.
        """
        self.t = t  # Grado minimo
        self.root = BTreeNode(t, True)  # Inizializza la radice come nodo foglia

        self.nodes_read = 0  #contatori per misurare le performance
        self.nodes_written = 0

    def search(self, k, node=None):
        """
        Cerca una chiave nel B-albero.

        :param k: Chiave da cercare.
        :param node: Nodo da cui iniziare la ricerca (default è la radice).
        :return: Nodo e indice della chiave, oppure None se la chiave non esiste.
        """
        if node is None:
            node = self.root
        self.nodes_read += 1  # Incrementa il contatore dei nodi letti
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1

        # Se la chiave è presente in questo nodo, restituiscila
        if i < len(node.keys) and node.keys[i] == k:
            return node, i

        # Se il nodo è una foglia, la chiave non è presente
        if node.is_leaf:
            return None

        # Se il nodo è interno, cerca nel figlio appropriato
        return self.search(k, node.children[i])

    def split_child(self, parent, i, full_child):
        """
                Divide un nodo figlio pieno in due nodi e sposta la chiave mediana nel nodo padre.

                :param parent: Nodo padre che contiene il full_child.
                :param i: Indice di full_child nel nodo parent.
                :param full_child: Nodo pieno da dividere.
        """

        t = self.t
        # Controllo: verifica che il nodo sia pieno
        if len(full_child.keys) != 2 * t - 1:
            raise ValueError(f"split_child chiamato su un nodo non pieno! Chiavi: {full_child.keys}")

        # Crea un nuovo nodo per le chiavi a destra della mediana
        new_child = BTreeNode(t, full_child.is_leaf)
        new_child.keys = full_child.keys[t:]
        if not full_child.is_leaf:
            new_child.children = full_child.children[t:]
        full_child.keys = full_child.keys[:t]
        full_child.children = full_child.children[:t]
        # Sposta la chiave mediana al genitore
        parent.children.insert(i + 1, new_child)
        parent.keys.insert(i, full_child.keys[t - 1])
        self.nodes_written += 1

    def insert_non_full(self, node, key):
        """
        Inserisce una chiave in un nodo che non è pieno.

        :param node: Nodo in cui inserire la chiave.
        :param key: Chiave da inserire.
        """

        i = len(node.keys) - 1
        self.nodes_read += 1  # Leggiamo il nodo corrente
        # Se il nodo è una foglia, inserisci la chiave nel punto corretto
        if node.is_leaf:
            node.keys.append(None)  # Aggiungi uno spazio per la nuova chiave
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
            self.nodes_written += 1  # Scriviamo nel nodo corrente
        else:
            # Trova il figlio corretto in cui inserire la chiave
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            # Se il figlio è pieno, dividilo e sposta la chiave mediana nel nodo corrente
            if node.children[i].is_full():
                self.split_child(node, i, node.children[i])
                self.nodes_written += 1  # Scriviamo nel nodo genitore
                # Dopo la divisione, la chiave mediana si trova in node.keys[i]
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def insert(self, key):
        """
        Inserisce una chiave nel B-albero.

        :param key: Chiave da inserire.
        """
        root = self.root
        # Se la radice è piena, bisogna dividere e creare una nuova radice
        if root.is_full():
            new_root = BTreeNode(self.t, False)
            new_root.children.append(self.root)
            self.split_child(new_root, 0, self.root)
            self.root = new_root
            self.nodes_written += 1  # Scriviamo un nuovo nodo (la nuova radice)
            self.insert_non_full(new_root, key)
        else:
            self.insert_non_full(root, key)
