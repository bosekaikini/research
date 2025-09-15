import math
import numpy as np
from itertools import permutations

actual_graphs_totals = [1, 1, 2, 4, 11, 34, 156, 1044, 12346, 274668, 
                        12005168, 1018997864, 165091172592, 50502031367952]
actual_ds_totals     = [1, 2, 4, 11, 32, 146, 934, 10624, 223629, 
                        9444529, 803666188, 134023600111]

my_ds_numbers = []
max_n = 7

def all_graphs(n):
    edges = n * (n - 1) // 2
    total = 1 << edges
    graphs = []
    for mask in range(total):
        mat = np.zeros((n, n), dtype=int)
        idx = 0
        for i in range(n):
            for j in range(i+1, n):
                if (mask >> idx) & 1:
                    mat[i, j] = mat[j, i] = 1
                idx += 1
        graphs.append(mat)
    return graphs

def degree_sequence(mat):
    return tuple(sorted(np.sum(mat, axis=1)))

def same_graph(A, B):
    n = len(A)
    for p in permutations(range(n)):
        perm_B = B[np.ix_(p, p)]
        if np.array_equal(A, perm_B):
            return True
    return False


def unlabeled_graphs(n):
    seen = []
    for G in all_graphs(n):
        degs = degree_sequence(G)
        new = True
        for H, h_degs in seen:
            if degs != h_degs:
                continue
            if same_graph(G, H):
                new = False
                break
        if new:
            seen.append((G, degs))
    return [g for g, _ in seen]

def count_ds_graph(n):
    my_ds_set = set()
    for G in unlabeled_graphs(n):
        my_ds_set.add(degree_sequence(G))
    my_ds_numbers.append(len(my_ds_set))

def data_output(my_ds_numbers, actual_ds_totals, max_n):
    for i in range(1, max_n+1):
        print(f"n={i}  computed={my_ds_numbers[i-1]}  actual={actual_ds_totals[i-1]}")

for n in range(1, max_n+1):
    count_ds_graph(n)

data_output(my_ds_numbers, actual_ds_totals, max_n)
