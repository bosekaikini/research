actual_ds_totals = [1, 2, 4, 11, 32, 146, 934, 10624, 223629, 9444529, 803666188, 134023600111]

max = 7
graph_set=set()

def convert_toString(matrix):
    eigenvals=""
    for i in matrix:
        eigenvals+=i
    return eigenvals

        
def compute_spectrum(graph):
    A=G.adjacency_matrix()
    return convert_toString(A.eigenvalues())
    

for G in graphs.nauty_geng(max):
    graph_set.add(compute_spectrum(G))

    
print("Expected: ",actual_ds_totals[max+1])
print("Actual: ",len(graph_set))
