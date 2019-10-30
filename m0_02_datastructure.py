"""Compute a path from boundary to boundary in a quad mesh
Parameters
----------
mesh [Mesh] - Quad Mesh Input
starting_vertex [int] - Vertice key of the starting point, 
    must be on a valid edge and not at corner.
Returns
-------
[list] - List of Vertice Keys

"""
def boundary_to_boundary_path(mesh, starting_vertex):
    # Large loop
    path = [starting_vertex]

    while(True):
        # Find neighbours of the last point
        neighbours = mesh.vertex_neighbors(path[-1], ordered=True)
        print (neighbours)
        
        # Pick one of the neighbours and continue
        next_index = 1
        if (len(path) > 1):
            next_index = neighbours.index(path[-2]) -2

        path.append(neighbours[next_index])

        # Terminate if that last picked neighbour is an edge
        if (mesh.is_vertex_on_boundary(path[-1]) ) : break
    
    return path

if __name__ == "__main__":
    import compas
    from compas.datastructures import Mesh
    from compas_plotters import MeshPlotter


    # Define input

    mesh = Mesh.from_obj(compas.get('faces.obj'))
    starting_vertex = 29

    # Compute path
    path = boundary_to_boundary_path (mesh, starting_vertex)

    # Visualize results
    plotter = MeshPlotter(mesh)
    plotter.draw_faces()
    plotter.draw_edges()
    plotter.draw_vertices(radius=0.2, text='key')
    # Green is the Picked Vertice
    plotter.draw_vertices(radius=0.3, text='key', keys=path[:1], facecolor=(0, 255, 0))
    # Red is the path
    plotter.draw_vertices(radius=0.3, text='key', keys=path[1:], facecolor=(255, 0, 0))
    plotter.show()

