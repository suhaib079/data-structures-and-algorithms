from trees.trees_max import *

def test_find_max_value():
    tree = Node(1)
    tree.data.left = Node(2)
    tree.data.right = Node(3)
    tree.data.left.left = Node(4)
    tree.data.left.right = Node(5)
    tree.data.right.left = Node(6)
    tree.data.right.right = Node(7)
    assert tree.Node.findMax() == 7