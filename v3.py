actual_ds_totals = [1, 2, 4, 11, 32, 146, 934, 10624, 223629, 9444529, 803666188, 134023600111]

num_vertices = 7
graph_map={}
count=0

def compute_spectrum(g):
    eigenvals=g.adjacency_matrix().eigenvalues()
    return tuple(sorted(eigenvals))

for g in graphs.nauty_geng(num_vertices):
    spec=compute_spectrum(g)
    if graph_map.get(spec):
        graph_map.update({spec:False})
    else:
        graph_map.update({spec:True})

for value in graph_map.values():
    if value==True:
        count+=1
    
print("Expected: ",actual_ds_totals[num_vertices-1])
print("Calculated: ",count)
