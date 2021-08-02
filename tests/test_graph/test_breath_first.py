from data_structures_and_algorithms.graph.graph import Graph
import pytest


def test_breadth_first():
    graph = Graph()
    A = graph.add_node('A')
    B = graph.add_node('B')
    C = graph.add_node('C')
    D = graph.add_node('D')
    E = graph.add_node('E')
    F = graph.add_node('F')
    G = graph.add_node('G')
    H = graph.add_node('H')
    I = graph.add_node('I')
    K = graph.add_node('K')
    graph.add_edge(A, B)
    graph.add_edge(A, C)
    graph.add_edge(A,E)
    graph.add_edge(B, D)
    graph.add_edge(C, F)
    graph.add_edge(C, B)
    graph.add_edge(E,G)
    graph.add_edge(F,H)
    graph.add_edge(G,H)
    graph.add_edge(F,I)
    graph.add_edge(H,K)
    graph.add_edge(I,K)
    assert len(graph.breadth_first_search(A)) == 10
    