def is_last(node):
    return not node.left and not node.right

def go_right(node):
    return node.right

def go_left(node):
    return node.left

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root , s):
    result = []
    node = root
    for char in s:
        if char == '1':
            node = go_right(node)
        elif char == '0':
            node = go_left(node)
        
        if is_last(node):
            result.append(node.data)
            node = root
            
    print (''.join(result))