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


def run_test(structure, keys):
    """
    Esegue un test di inserimento per una struttura dati.

    :param structure: Istanza della struttura dati (BTree o BinarySearchTree).
    :param keys: Lista di chiavi da inserire.
    :return: Tuple (nodi_letti, nodi_scritti, tempo_inserimento).
    """
    start_time = time.time()
    for key in keys:
        structure.insert(key)
    end_time = time.time()

    return structure.nodes_read, structure.nodes_written, end_time - start_time


def main():
    key_counts = [100, 500, 1000, 5000]  # Numero di chiavi da testare
    modes = ["linear", "random"]  # Modalità di generazione delle chiavi

    results = {
        "btree": {mode: {"reads": [], "writes": [], "times": [], "total_accesses": []} for mode in modes},
        "bst": {mode: {"reads": [], "writes": [], "times": [], "total_accesses": []} for mode in modes}
    }

    for mode in modes:
        for count in key_counts:
            # Genera le chiavi
            keys = generate_keys(count, mode)

            # Testa il B-Tree
            b_tree = BTree(t=5)
            btree_reads, btree_writes, btree_time = run_test(b_tree, keys)
            results["btree"][mode]["reads"].append(btree_reads)
            results["btree"][mode]["writes"].append(btree_writes)
            results["btree"][mode]["times"].append(btree_time)
            results["btree"][mode]["total_accesses"].append(btree_reads + btree_writes)

            # Testa il BST
            bst = BinarySearchTree()
            bst_reads, bst_writes, bst_time = run_test(bst, keys)
            results["bst"][mode]["reads"].append(bst_reads)
            results["bst"][mode]["writes"].append(bst_writes)
            results["bst"][mode]["times"].append(bst_time)
            results["bst"][mode]["total_accesses"].append(bst_reads + bst_writes)

    # Genera i grafici
    for mode in modes:
        for metric in ["reads", "writes", "times", "total_accesses"]:
            plt.figure()
            plt.plot(key_counts, results["btree"][mode][metric], label="B-Tree", marker="o")
            plt.plot(key_counts, results["bst"][mode][metric], label="BST", marker="o")
            plt.title(f"{metric.capitalize()} ({mode.capitalize()} Keys)")
            plt.xlabel("Number of Keys")
            plt.ylabel(metric.capitalize())
            plt.legend()
            plt.grid()
            plt.savefig(f"{metric}_{mode}.png")
            plt.show()


if __name__ == "__main__":
    main()
