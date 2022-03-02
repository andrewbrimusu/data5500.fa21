
import random
import time
# Python program to demonstrate delete operation
# in binary search tree

from print_tree import *

# A Binary Tree Node

class Node:

	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# A utility function to insert a
# new node with given key in BST
def insert(node, key):

	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	# return the (unchanged) node pointer
	return node
	
	
# Task 1. Write a function to find the minimum value in the tree


# Task 2. Write a recursive findMin function

    
# Task 3. Write a findMaxRecursive


# print tree inorder
def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key, end=" ")
		inorder(root.right)
 
# Task 4. Write a pre-order print


# Task 5. Write a post-order print

		

# Given a binary search tree and a key, this function
# delete the key and returns the new root


def deleteNode(root, key):

	# Base Case
	if root is None:
		return root

	# If the key to be deleted 
	# is smaller than the root's
	# key then it lies in left subtree
	if key < root.key:
		root.left = deleteNode(root.left, key)

	# If the kye to be delete 
	# is greater than the root's key
	# then it lies in right subtree
	elif(key > root.key):
		root.right = deleteNode(root.right, key)

	# If key is same as root's key, then this is the node
	# to be deleted
	else:

		# Node with only one child or no child
		if root.left is None:
			temp = root.right
			root = None
			return temp

		elif root.right is None:
			temp = root.left
			root = None
			return temp

		# Node with two children: 
		# Get the inorder successor
		# (smallest in the right subtree)
		temp = minValueNode(root.right)

		# Copy the inorder successor's 
		# content to this node
		root.key = temp.key

		# Delete the inorder successor
		root.right = deleteNode(root.right, temp.key)

	return root

# Task 6. write a findval recursive function




def main():
    # creating a Tree with root variable "root"
    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)
    
    # finding values in the tree
    # print(findval(root, 80))
    # print(findval(root, 10))
    
    # traversing the tree
    print("Inorder traversal of the given tree")
    inorder(root)
    # PrintTree(root)
    
    # deleting 
    print("\nDelete 20")
    root = deleteNode(root, 20)
    print("Inorder traversal of the modified tree")
    inorder(root)
    
    print("\nDelete 30")
    root = deleteNode(root, 30)
    print("Inorder traversal of the modified tree")
    inorder(root)
    
    print("\nDelete 50")
    root = deleteNode(root, 50)
    print("Inorder traversal of the modified tree")
    inorder(root)
    
    display(root)
    
    
    tree2 = None
    tree2 = insert(tree2, 3)
    tree2 = insert(tree2, 1)
    tree2 = insert(tree2, 4)
    tree2 = insert(tree2, 2)
    tree2 = insert(tree2, 5)
    tree2 = insert(tree2, 9)
    
    display(tree2)
    inorder(tree2)
    print()
    preorder(tree2)
    print()
    postorder(tree2)
    
    print("\nmin value: ", findMin(tree2).key)
    print("\nmin value recursive: ", findMinRec(tree2).key)
   
            
        
    # create a list of 10000 numbers
    # lst = [random.randint(1,10000) for i in range(1000000)]
    # # each number is a random number between 1 and 10000 random.randint(1,10000)
    
    # # in other loop for in 1 to 10000, check to see if i is in the list
    # start1 = time.time()
    # for i in range(1,10001):
    #     for l in lst:
    #         if i == l:
    #             break
    # end1 = time.time()
    # print("search time list (sec): ", end1-start1)
    
    
    
    # root = None
    # for i in range(1000000):
    #     root = insert(root, random.randint(1,10000))
        
    
    # start = time.time()
    # for i in range(10000):
    #     findval(root, i)
    # end = time.time()
    
    # print("search time tree (sec): ",end-start)
    
    # print("---------------------")
    
    
main()