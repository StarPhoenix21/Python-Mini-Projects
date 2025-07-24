class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.val:
            if self.left is None:
                self.left = BSTNode(data)
                return f"Inserted {data} to left of {self.val}"
            else:
                return self.left.insert(data)
        elif data > self.val:
            if self.right is None:
                self.right = BSTNode(data)
                return f"Inserted {data} to right of {self.val}"
            else:
                return self.right.insert(data)
        else:
            return f"Insertion failed: {data} already exists"

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current

    def delete(self, data):
        if data < self.val:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.val:
            if self.right:
                self.right = self.right.delete(data)
        else:
            # Node found
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_larger_node = self.right.find_min()
                self.val = min_larger_node.val
                self.right = self.right.delete(min_larger_node.val)
        return self

    def inorder(self):
        result = []
        if self.left:
            result.extend(self.left.inorder())
        result.append(self.val)
        if self.right:
            result.extend(self.right.inorder())
        return result

    def __str__(self):
        return " -> ".join(map(str, self.inorder()))


class BinarySearchTree:
    def __init__(self, root_val):
        self.root = BSTNode(root_val)

    def insert(self, data):
        return self.root.insert(data)

    def delete(self, data):
        self.root = self.root.delete(data)

    def display(self):
        return str(self.root)


if __name__ == "__main__":
    tree = BinarySearchTree(50)
    print(tree.insert(30))
    print(tree.insert(70))
    print(tree.insert(20))
    print(tree.insert(40))
    print(tree.insert(60))
    print(tree.insert(80))

    print("Initial tree:", tree.display())

    tree.delete(70)
    print("After deleting 70:", tree.display())

    tree.delete(50)
    print("After deleting root (50):", tree.display())


        
    
    
