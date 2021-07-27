from insertion_sort.insertion_sort import tree_intersection,Node,BinaryTree
import pytest

@pytest.fixture
def fir_tree():
    Bt1 = BinaryTree()
    Bt1.root = Node(6)
    Bt1.root.right = Node(9)
    Bt1.root.left = Node(2)
    Bt1.root.left.left = Node(0)
    Bt1.root.right.left = Node(10)
    return Bt1


@pytest.fixture
def sec_tree():
    Bt2 = BinaryTree()
    Bt2.root = Node(6)
    Bt2.root.right = Node(2)
    Bt2.root.left = Node(10)
    Bt2.root.left.left = Node(18) 
    return Bt2


def test_intersection(fir_tree, sec_tree):

    actual=tree_intersection(fir_tree, sec_tree)
    
    assert actual == {2, 10, 6}