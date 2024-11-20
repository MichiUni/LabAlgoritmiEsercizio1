import random
import time
import matplotlib.pyplot as plt
from btree.b_tree import BTree
from binary_search_tree.bst import BinarySearchTree


def generate_keys(count, mode="linear"):
    """
    Genera una lista di chiavi.

    :param count: Numero di chiavi da generare.
    :param mode: 'linear' per chiavi in ordine crescente, 'random' per ordine casuale.
    :return: Lista di chiavi.
    """
    if mode == "linear":
        return list(range(1, count + 1))
    elif mode == "random":
        return random.sample(range(1, count + 1), count)


def run_search_test(structure, keys_to_search):
    """
    Esegue un test di ricerca per una struttura dati.

    :param structure: Istanza della struttura dati (BTree o BinarySearchTree).
    :param keys_to_search: Lista di chiavi da cercare.
    :return: Tuple (nodi_letti, tempo_ricerca).
    """
    start_time = time.time()
    for key in keys_to_search:
        structure.search(key)
    end_time = time.time()

    return structure.nodes_read, end_time - start_time


def main():
    key_counts = [100, 500, 1000, 5000]  # Numero di chiavi da testare
    modes = ["linear", "random"]  # Modalità di generazione delle chiavi

    results = {
        "btree": {mode: {"reads": [], "times": []} for mode in modes},
        "bst": {mode: {"reads": [], "times": []} for mode in modes}
    }

    for mode in modes:
        for count in key_counts:
            # Genera le chiavi da inserire
            keys = generate_keys(count, mode)

            # Testa il B-Tree
            b_tree = BTree(t=5)
            for key in keys:
                b_tree.insert(key)

            # Genera chiavi da cercare (50% presenti, 50% non presenti)
            keys_to_search = random.sample(keys, len(keys) // 2) + \
                             random.sample(range(max(keys) + 1, max(keys) + len(keys) // 2 + 1), len(keys) // 2)

            btree_reads, btree_time = run_search_test(b_tree, keys_to_search)
            results["btree"][mode]["reads"].append(btree_reads)
            results["btree"][mode]["times"].append(btree_time)

            # Testa il BST
            bst = BinarySearchTree()
            for key in keys:
                bst.insert(key)

            bst_reads, bst_time = run_search_test(bst, keys_to_search)
            results["bst"][mode]["reads"].append(bst_reads)
            results["bst"][mode]["times"].append(bst_time)

    # Genera i grafici
    for mode in modes:
        for metric in ["reads", "times"]:
            plt.figure()
            plt.plot(key_counts, results["btree"][mode][metric], label="B-Tree", marker="o")
            plt.plot(key_counts, results["bst"][mode][metric], label="BST", marker="o")
            plt.title(f"{metric.capitalize()} ({mode.capitalize()} Keys)")
            plt.xlabel("Number of Keys")
            plt.ylabel(metric.capitalize())
            plt.legend()
            plt.grid()
            plt.savefig(f"{metric}_search_{mode}.png")
            plt.show()


if __name__ == "__main__":
    main()
