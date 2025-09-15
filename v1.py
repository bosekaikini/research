actual_graphs_totals = [1, 1, 2, 4, 11, 34, 156, 1044, 12346, 274668, 12005168, 1018997864, 165091172592, 50502031367952]
actual_ds_totals     = [1, 2, 4, 11, 32, 146, 934, 10624, 223629, 9444529, 803666188, 134023600111]

my_ds_numbers = []
max_n = 7


def sqrt(x):
    """Newton’s method for square root (no math import)."""
    if x == 0: return 0
    guess = x
    for _ in range(20):
        guess = 0.5 * (guess + x / guess)
    return guess

def normalize_vector(v):
    s = sum(x*x for x in v)
    s = sqrt(s)
    if s == 0: return v
    return [x/s for x in v]

# -----------------------------
# Graph utilities
# -----------------------------

def all_graphs(n):
    """Generate all graphs on n vertices (adjacency matrices, no loops)."""
    edges = n*(n-1)//2
    total = 1 << edges
    graphs = []
    for mask in range(total):
        mat = [[0]*n for _ in range(n)]
        idx = 0
        for i in range(n):
            for j in range(i+1,n):
                if (mask >> idx) & 1:
                    mat[i][j] = mat[j][i] = 1
                idx += 1
        graphs.append(mat)
    return graphs

def degree_sequence(mat):
    return sorted([sum(row) for row in mat])

def same_graph(A,B):
    """Check isomorphism by brute-force relabeling (slow but ok for small n)."""
    n = len(A)
    from itertools import permutations
    for p in permutations(range(n)):
        ok = True
        for i in range(n):
            for j in range(n):
                if A[i][j] != B[p[i]][p[j]]:
                    ok = False
                    break
            if not ok: break
        if ok: return True
    return False

def unlabeled_graphs(n):
    seen = []
    for G in all_graphs(n):
        degs = degree_sequence(G)
        new = True
        for H, h_degs in seen:
            if degs != h_degs:
                continue
            if same_graph(G,H):
                new = False
                break
        if new:
            seen.append((G,degs))
    return [g for g,_ in seen]


def compute_spectrum(mat):
    return str(sorted(degree_sequence(mat)))

def count_ds_graph(n):
    my_ds_set = set()
    for G in unlabeled_graphs(n):
        my_ds_set.add(compute_spectrum(G))
    my_ds_numbers.append(len(my_ds_set))

def data_output(my_ds_numbers, actual_ds_totals, max_n):
    for i in range(1, max_n+1):
        print("n=", i, " computed=", my_ds_numbers[i-1], " actual=", actual_ds_totals[i-1])


for n in range(1, max_n+1):
    count_ds_graph(n)

data_output(my_ds_numbers, actual_ds_totals, max_n)