from data_structures_and_algorithms.graph.graph import Graph


def test_node_can_be_added_to_graph():
    g = Graph()
    g.add_node('suhaib')
    actual = g.get_nodes()
    expected = {'suhaib': []}
    assert expected == actual

def test_edge_added_to_graph():
    g=Graph()
    g.add_node('suhaib')
    g.add_node('emad')
    g.add_edge('suhaib', 'emad', 1)

    actual = g.get_neighbors('suhaib')
    expected = 'suhaib --> emad edge weight: 1'
    assert actual == expected

def test_collection_of_nodes_properly_retrived():
    g = Graph()
    g.add_node('suhaib')
    g.add_node('emad')
    g.add_node('hussen')
    actual = g.get_nodes()
    expected = {'suhaib': [],'emad': [],'hussen': []}
    assert expected == actual

def test_all_neighbors_can_be_retrived():
    g = Graph()
    g.add_node('suhaib')
    g.add_node('emad')
    g.add_node('hussen')
    g.add_node('abdennabi')

    g.add_edge('suhaib', 'emad', 1)
    g.add_edge('suhaib', 'abdennabi', 3)
    g.add_edge('emad', 'abdennabi', 4)
    g.add_edge('abdennabi', 'abdennabi', 6)
    g.add_edge('abdennabi', 'suhaib', 5)
    actual = g.get_nodes()
    expected = {'suhaib': [['emad', 1], ['abdennabi', 3]], 'emad': [['abdennabi', 4]], 'hussen': [], 'abdennabi': [['abdennabi', 6], ['suhaib', 5]]}
    assert expected == actual

def test_all_neighbors_can_be_retrived_with_weight():
    g = Graph()
    g.add_node('suhaib')
    g.add_node('emad')

    g.add_edge('suhaib','emad',4)

    actual = g.get_neighbors('suhaib')
    expected = 'suhaib --> emad edge weight: 4'

    assert expected == actual

def test_proper_size_is_returned():
    g = Graph()
    g.add_node('suhaib')
    g.add_node('emad')
    g.add_node('hussen')
    g.add_node('abdennabi')

    actual = g.size()
    expected = 4
    assert expected == actual

def test_one_node_one_edge():
    g = Graph()
    g.add_node('suhaib')

    g.add_edge('suhaib','suhaib')
    actual = g.get_neighbors('suhaib')
    expected = 'suhaib --> suhaib edge weight: 1'
    assert expected == actual
def test_empty_graph_return_none():
    g = Graph()
    actual = g.get_nodes()
    excepted = None
    assert excepted == actual