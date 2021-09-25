import time
import random
start=time.time()
end=time.time()
print("time (sec): ",end-start)

def findval(root, lkpval):
    if lkpval < root.key:
        if root.left is None:
            return str(lkpval)+" Not Found"
        return findval(root.left, lkpval)
    elif lkpval > root.key:
        if root.right is None:
            return str(lkpval)+" Not Found"
        return findval(root.right, lkpval)
    else:
        return str(root.key) + ' is found'
        