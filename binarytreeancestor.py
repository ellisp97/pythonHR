class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self,val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val<current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val>current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    def getHeight(self, root):
        if root == None:
            return -1
        else:
            return 1 + max( self.getHeight(root.left), self.getHeight(root.right) )



    # Python 3 iterative solution
    def lca(self,root , v1 , v2):
        # make sure v2 > v1
        if v1 > v2: 
            v1, v2 = v2, v1
        # traverse until terminal
        while True:
            if v1 < root.info and v2 < root.info:
                root = root.left
            elif v1 > root.info and v2 > root.info:
                root = root.right
            else:
                return(root.info)

tree = BinarySearchTree()
t = int(input())
arr = list(map(int, input().split()))
v1,v2 = map(int, input().split())

for i in range(t):
    tree.create(arr[i])

print(tree.lca(tree.root,v1,v2))

