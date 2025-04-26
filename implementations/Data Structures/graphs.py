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
                new_paths = self.get_paths(node, end, path) # new_paths is a list of paths from the current node to the end node

                for new_path in new_paths:
                    if new_path not in path: # Avoid cycles in the path
                        paths.append(new_path)

        return paths
    
    def get_shortest_path(self, start, end):
        all_paths = self.get_paths(start, end)
        if not all_paths:
            return None
        shortest_path = min(all_paths, key=len)
        return shortest_path
        

if __name__ == "__main__":
    # Tuple of flight routes (start, end)
    routes = (
        ("New York", "Los Angeles"),
        ("Los Angeles", "Chicago"),
        ("Chicago", "Houston"),
        ("Houston", "Miami"),
        ("Miami", "New York"),
        ("Los Angeles", "Miami"),
        ("Chicago", "Los Angeles")
    )
    
    route_graph = Graph(routes)

    start_city = "New York"
    end_city = "Miami"
    
    # Get all paths and shortest path from start_city to end_city
    # The get_paths method returns all paths from start to end, while the get_shortest_path method returns the shortest path
    all_paths = route_graph.get_paths(start_city, end_city)
    if all_paths:
        print(f"All paths from {start_city} to {end_city}:")
        for path in all_paths:
            print(" -> ".join(path))  

    shortest_path = route_graph.get_shortest_path(start_city, end_city)
    if shortest_path:
        print(f"Shortest path from {start_city} to {end_city}: {' -> '.join(shortest_path)}")
    else:
        print(f"No path found from {start_city} to {end_city}.")

    



    

  


