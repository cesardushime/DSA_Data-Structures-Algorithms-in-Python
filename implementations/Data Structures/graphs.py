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



    

  


