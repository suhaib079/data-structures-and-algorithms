from insertion_sort.insertion_sort import tree_intersection,Node,BinaryTree
import pytest

@pytest.fixture
def fir_tree():
    Bt1 = BinaryTree()
    Bt1.root = Node(8)
    Bt1.root.right = Node(13)
    Bt1.root.left = Node(65)
    Bt1.root.left.left = Node(1)
    Bt1.root.right.left = Node(70)
    return Bt1


@pytest.fixture
def sec_tree():
    Bt2 = BinaryTree()
    Bt2.root = Node(8)
    Bt2.root.right = Node(65)
    Bt2.root.left = Node(1)
    Bt2.root.left.left = Node(22) 
    return Bt2


def test_intersection(fir_tree, sec_tree):

    actual=tree_intersection(fir_tree, sec_tree)
    
    assert actual == {8, 65, 1}