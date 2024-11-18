class BTreeNode:
    def __init__(self, t, is_leaf):
        """
        Inizializza un nuovo nodo di un B-albero.

        :param t: Il grado minimo del B-albero.
        :param is_leaf: Booleano, True se il nodo è una foglia.
        """
        self.t = t  # Grado minimo
        self.is_leaf = is_leaf  # Indica se è una foglia
        self.keys = []  # Lista delle chiavi
        self.children = []  # Lista dei figli (solo per nodi interni)

    def is_full(self):
        """
        Ritorna True se il nodo è pieno, ovvero contiene 2 * t - 1 chiavi.
        """
        return len(self.keys) == 2 * self.t - 1
