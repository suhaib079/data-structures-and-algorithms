  
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
  
    def findMax(root):
        if (root == None):
            return float('-inf')
        
        res = root.data
        left_max = Node.findMax(root.left)
        right_max = Node.findMax(root.right)
        if (left_max > res):
            res = left_max
        if (right_max > res):
            res = right_max
        return res
  
  

if __name__ == '__main__':
    root = Node(4)
    root.left = Node(8)
    root.right = Node(14)
    root.left.right = Node(20)
    root.left.right.left = Node(10)
    root.left.right.right = Node(99)
    root.right.right = Node(88)
    root.right.right.left = Node(65)
  
    
    print(Node.findMax(root))
  