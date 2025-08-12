![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)


#    Binary Search Tree (BST) Implementation in Python
![Alt text](https://i.pinimg.com/originals/e7/f5/b6/e7f5b60413ff4bedebfd2805f97d8de7.jpg)  

##   Overview
A **Binary Search Tree (BST)** is a special kind of **Binary Tree** with one key property:  
- The **left subtree** of a node contains values **less than** the node’s value.  
- The **right subtree** of a node contains values **greater than** the node’s value.  
- **All values in a BST must be unique**.

This project provides a **Python implementation** of a BST, allowing you to **insert**, **remove**, **search**, and **traverse** nodes while maintaining the BST property.

---

##   Features
-   **Initialization** — Create a BST with a given root node and optional left/right subtrees.
-   **Add** — Insert a new value while keeping the BST property intact.
-   **Remove** — Delete a value and restructure the tree if needed.
-   **Search** — Find if a value exists in the tree.
-   **Traversal** — Inorder, Preorder, and Postorder printing.

---

##   BST Property Rule  

For any node N:  
  All values in N's left subtree  <  N.value  
  All values in N's right subtree >  N.value  
```python
from bst import BST  # assuming file is bst.py

#   Initialize the BST
tree = BST(1, None, None)  
print("Initial Tree:")
tree.print_inorder()  # Output: 1

#  Add elements
print(tree.add(4))  # Adds 4 as the right child
print(tree.add(0))  # Adds 0 as the left child
tree.print_inorder()  # Output: 0 1 4

#   Remove elements
print(tree.remove(1))  # Removes 1, restructures tree
tree.print_inorder()  # Output: 0 4

#   Search
print(tree.search(4))  # True
print(tree.search(10)) # False
# Initial Insertion: 1, 4, 0
    1
   / \
  0   4
# After Removing 1:
    4
   /
  0
#Time Complexity

| Operation  | Average Case | Worst Case |
| ---------- | ------------ | ---------- |
| **Search** | O(log n)     | O(n)       |
| **Insert** | O(log n)     | O(n)       |
| **Delete** | O(log n)     | O(n)       |




# Author
[Tomas Urdinola](https://github.com/tomurdi)
