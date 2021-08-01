class Node:
    def __init__(self, value):
        self.value = value

class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        node = Node(value)
        if value in self._adjacency_list:
            print('Vertex',value,' value exists')
        self._adjacency_list[node.value] = []

    def add_edge(self, start_node, end_node, weight=1):
        if start_node not in self._adjacency_list.keys():
           print("Vertex ", start_node, " value not exist")
        elif end_node not in self._adjacency_list.keys():
            print("Vertex ", end_node, " value not exist")
        else:
            temp = [end_node, weight]
            self._adjacency_list[start_node].append(temp)

    def get_nodes(self):

        if len(self._adjacency_list) == 0:
            return None
        else:
            return self._adjacency_list

    def get_neighbors(self, node):
        for edges in self._adjacency_list[node]:
               return f"{node} --> {edges[0]} edge weight: {edges[1]}"

    def size(self):
        return len(self._adjacency_list)

if __name__ == "__main__":
    graph = Graph()
    graph.add_node('suhaib')
    graph.add_node('emad')
    graph.add_node('hussen')
    graph.add_node('abdennabi')

    graph.add_edge('suhaib', 'emad', 1)
    graph.add_edge('suhaib', 'abdennabi', 3)
    graph.add_edge('emad', 'abdennabi', 4)
    graph.add_edge('abdennabi', 'abdennabi', 6)
    graph.add_edge('abdennabi', 'suhaib', 5)
    print(graph.get_nodes())

    print(graph.get_neighbors('suhaib'))
    print(graph.size())






