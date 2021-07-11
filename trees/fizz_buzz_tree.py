class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.pre_order(self.root, "")
        elif traversal_type == "inorder":
            return self.in_order(self.root, "")
        elif traversal_type == "postorder":
            return self.post_order(self.root, "")
        elif traversal_type == 'breadthfirst':
            return self.breadth_first(self.root)
        else:
            print("Traversal type not supported")
            return False

    def pre_order(self, start, traversal):
        
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.pre_order(start.left, traversal)
            traversal = self.pre_order(start.right, traversal)
        return traversal

    def in_order(self, start, traversal):
        
        if start:
            traversal = self.in_order(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.in_order(start.right, traversal)
        return traversal

    def post_order(self, start, traversal):
        
        if start:
            traversal = self.post_order(start.left, traversal)
            traversal = self.post_order(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

def fizz_buzz_tree(tree):

  
    tree = tree.print_tree('preorder')
    if tree == None or tree == "None-":
        return "Tree is empty"
    else:
        x= tree.split('-')
        y= x.remove('')
        new_tree =[]
        for i in range(len(x)):
            if int(x[i]) % 3 ==0 and int(x[i]) %5  == 0:
                new_tree.append('FizzBuzz')
            elif int(x[i]) % 3 == 0:
                new_tree.append('Fizz')
            elif int(x[i]) % 5 == 0:
                new_tree.append('Buzz')
            else:
                new_tree.append(x[i])
    return new_tree



if __name__ == "__main__":

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(6)
    tree.root.left.left = Node(8)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(12)
    tree.root.right.right = Node(18)
    print(fizz_buzz_tree(tree))