class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

    def pre_order(self,start,traversal):   #root>left>right
        if start:
            traversal=traversal+(str(start.val)+'->')
            traversal=self.pre_order(start.left,traversal)
            traversal=self.pre_order(start.right,traversal)
        return traversal

    def in_order(self, start, traversal):  #Left>root>right
        if start:
            traversal = self.in_order(start.left, traversal)
            traversal += (str(start.val) + "->")
            traversal = self.in_order(start.right, traversal)
        return traversal

    def post_order(self, start, traversal): #Left->Right->Root
        if start:
            traversal = self.post_order(start.left, traversal)
            traversal = self.post_order(start.right, traversal)
            traversal += (str(start.val) + "->")
        return traversal

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.pre_order(self.root, "")
        elif traversal_type == "inorder":
            return self.in_order(self.root, "")
        elif traversal_type == "postorder":
            return self.post_order(self.root, "")

        else:
            print("Traversal type error ")
            return False

       
    class Binary_search:
      def __init__(self, root=None):
        self.root = root
        self.tree_list = []
        self.val = False

    def add(self, val, root=None):
        self.tree_list = []
        def adding_function(val):
            self.root=None
            if not self.root:
                self.root = Node(val)
            elif not root:
                adding_function(val, self.root)

            else:
                self.tree_list.append(root.val)
                if val < root.val:
                    if not root.left:
                        root.left = Node(val)
                        self.tree_list.append(root.left.val)
                    else:
                        adding_function(val, root.left)
                if val > root.val:
                    if not root.right:
                        root.right = Node(val)
                        self.tree_list.append(root.right.val)
                    else:
                        adding_function(val, root.right)
        adding_function(val)
        return self.tree_list




    def contains(self, val, root=None):
        if not self.root:
            raise Exception('empty tree')
        elif not root:
            self.contains(val, self.root)

        else:
            if val == root.val:
                self.val = True
            if val < root.val:
                if not root.left:
                    self.val = False
                else:
                    self.contains(val, root.left)
            if val > root.val:
                if not root.right:
                    self.val = False
                else:
                    self.contains(val, root.right)

        return self.val

    def __str__(self):

        items = []

        if self.tree_list == []:
            return 'empty tree'
        else:
            for i in self.tree_list:
                items.append(str(i))
        return '\n'.join(items)



