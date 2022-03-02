	
# Task 1. Write a function to find the minimum value in the tree
def findMin(node):
    # loop down to find the leftmost leaf
    while(node.left is not None):
    	node = node.left
    
    return node

# Task 2. Write a recursive findMin function
def findMinRec(node):
    if node.left == None:
        return node
    return node.left
    
# Task 3. Write a findMaxRecursive


# print tree inorder
def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key, end=" ")
		inorder(root.right)
 
# Task 4. Write a pre-order print
# A utility function to do inorder traversal of BST
def preorder(root):
	if root is not None:
		print(root.key, end=" ")
		preorder(root.left)
		preorder(root.right)

# Task 5. Write a post-order print
# A utility function to do inorder traversal of BST
def postorder(root):
	if root is not None:
		postorder(root.left)
		postorder(root.right)
		print(root.key, end=" ")
		
# Task 6 write a findval recursive
def findval(root, find_val):
	if root is not None:
		findval(root.left, find_val)
		if root.key == find_val:
		    return
		findval(root.right, find_val)