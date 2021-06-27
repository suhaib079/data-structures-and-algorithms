from trees.trees import *


def test_single_root_node():
    tree = BinaryTree(1)
    assert tree.root.val == 1
def test_pre_order():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    assert tree.print_tree("preorder") == '1->2->4->5->3->6->7->'
def test_in_order():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    assert tree.print_tree("inorder") == '4->2->5->1->6->3->7->'
def test_post_order():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    assert tree.print_tree("postorder") == '4->5->2->6->7->3->1->'