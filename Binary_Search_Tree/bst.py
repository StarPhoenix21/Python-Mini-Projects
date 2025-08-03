class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, root, data):
        if root is None:
            return BST(data)
        if data < root.val:
            root.left = self.insert(root.left, data)
        elif data > root.val:
            root.right = self.insert(root.right, data)
        return root

    def find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, data):
        if root is None:
            return root
        if data < root.val:
            root.left = self.delete(root.left, data)
        elif data > root.val:
            root.right = self.delete(root.right, data)
        else:
            # Node with one or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children
            min_node = self.find_min(root.right)
            root.val = min_node.val
            root.right = self.delete(root.right, min_node.val)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=' ')
            self.inorder(root.right)
