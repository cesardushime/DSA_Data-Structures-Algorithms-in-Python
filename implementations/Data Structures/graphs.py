# Flight Routes Graph
# This code implements a graph to represent flight routes between cities.


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print("Graph initialized with edges:", self.graph_dict)

    def get_paths(self, start, end, path=[]):

        path = path + [start]
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = []
        for node in self.graph_dict[start]: # Traverse the graph by going through the edges and nodes to find the path
            if node not in path: # Avoid cycles in the path (path is a list of nodes already visited)
                new_paths = self.get_paths(node, end, path) # path is the same as the previous path, but with the new node added to it

                for new_path in new_paths:
                    if new_path not in path: # Avoid cycles in the path
                        paths.append(new_path)

        return paths
        

if __name__ == "__main__":
    # Tuple of flight routes (start, end)
    routes = (
        ("New York", "Los Angeles"),
        ("Los Angeles", "Chicago"),
        ("Chicago", "Houston"),
        ("Houston", "Miami"),
        ("Miami", "New York"),
        ("Los Angeles", "Miami"),
        ("Chicago", "Los Angeles"),
    )
    
    route_graph = Graph(routes)

    



    

  


