from data_structures_and_algorithms.graph.depth_first import depth_first


def test_returning_the_correct_path():
     graph = {"A": ["B", "C", "D"],
             "B": ["E"],
             "C": ["F", "G"],
             "D": ["H"],
             "E": ["I"],
             "F": ["J"]}

     actual = depth_first(graph, "A")
     expected = ['A', 'B', 'E', 'I', 'C', 'F', 'J', 'G', 'D', 'H']
     assert actual == expected

def test_pasing_empty_graph():
    potato={}
    actual = depth_first(potato,'A',path=[])
    expected = ['A']
    assert expected == actual