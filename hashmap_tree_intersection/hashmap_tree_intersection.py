class Node:
    def __init__(self, data=None, left=None, right=None, next=None):
        self.data = data
        self.left = left
        self.right = right
        self.next = next

class BinaryTree:
    def __init__(self):
        self.root = None 


    def pre_order(self): 
        output = []
        def traverse(node):
            output.append(node.data)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(self.root)
        return output

  


def tree_intersection(tree1,tree2):
   

    list1 = tree1.pre_order()
    list2 = tree2.pre_order()
    lst = []
    for i in list1:
        for j in list2:
            if i == j:
                lst.append(i)
                j =+1
        i +=1 

    return set(lst)

    

if __name__ == "__main__":
    binary_tree1 = BinaryTree()
    binary_tree1.root = Node(8)
    binary_tree1.root.right = Node(12)
    binary_tree1.root.left = Node(2)
    binary_tree1.root.left.left = Node(99)
    binary_tree1.root.right.left = Node(10)

    binary_tree2 = BinaryTree()
    binary_tree2.root = Node(6)
    binary_tree2.root.right = Node(12)
    binary_tree2.root.left = Node(10)
    binary_tree2.root.left.left = Node(89)



    print(tree_intersection(binary_tree1,binary_tree2)) 