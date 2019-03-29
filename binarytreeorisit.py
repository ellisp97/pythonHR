from numpy import inf

def checkBST(root,min,max):
    if root == None:
        return True

    if root.data <= min or root.data >= max:
        return False

    # check recursively for every node.  
    return checkBST(root.left, min, root.data) and checkBST(root.right, root.data, max) 




tree = BinarySearchTree()
t = int(input())
arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

checkBST(tree.root,float(-inf),float(+inf))


#  This solution uses a Stack over recursion

# def checkBST(root):
#     if root is None:
#         return True
#     stack = [(float('-inf'), root, float('+inf'))]
#     while stack:
#         mind, node, maxd = stack.pop()
#         if not (mind < node.data < maxd):
#             return False
#         if node.left is not None:
#             stack.append((mind, node.left, node.data))
#         if node.right is not None: 
#             stack.append((node.data, node.right, maxd))
#     return True