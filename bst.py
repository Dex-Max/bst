import json

# DO NOT MODIFY THIS CLASS!
class Node():
    def  __init__(self, 
                  key        = None, 
                  leftchild  = None,
                  rightchild = None):
        self.key        = key
        self.leftchild  = leftchild
        self.rightchild = rightchild

# DO NOT MODIFY THIS FUNCTION!
# For the tree rooted at root, dump the tree to stringified JSON object and return.
# NOTE: in future projects you'll need to write the dump code yourself,
# but here it's given to you.
def dump(root: Node) -> str:
    def _to_dict(node) -> dict:    
        return {
            "k": node.key,
            "l": (_to_dict(node.leftchild) if node.leftchild is not None else None),
            "r": (_to_dict(node.rightchild) if node.rightchild is not None else None)
        }
    if root == None:
        dict_repr = {}
    else:
        dict_repr = _to_dict(root)
    return json.dumps(dict_repr)

#---------------------------------------------------------------------------------------------------

# For the tree rooted at root, insert the given key and return the root node.
# The key is guaranteed to not be in the tree.
def insert(root: Node, key: int) -> Node:
    if root == None:
        root = Node(key, None, None)
    elif key < root.key:
        if root.leftchild == None:
            root.leftchild = Node(key, None, None)
        else:
            insert(root.leftchild, key)
    elif key > root.key:
        if root.rightchild == None:
            root.rightchild = Node(key, None, None)
        else:
            insert(root.rightchild, key)

    return root

def search_min(root: Node) -> Node:
    if root.leftchild == None:
        return root
    else:
        return search_min(root.leftchild)


# For the tree rooted at root, delete the given key and return the root node.
# The key is guaranteed to be in the tree.
# When replacement is necessary use the inorder successor.
def delete(root: Node, key: int) -> Node:
    if root.key ==  key:
        if root.leftchild == None and root.rightchild == None:
            root = None
        elif root.leftchild != None and root.rightchild != None:
            min = search_min(root.rightchild)
            delete(root, min.key)
            root.key = min.key
        elif root.leftchild != None:
            root = root.leftchild
        else:
            root = root.rightchild
    elif key < root.key:
        root.leftchild = delete(root.leftchild, key)
    else:
        root.rightchild = delete(root.rightchild, key)
            
    return root

# For the tree rooted at root, calculate the list of keys on the path from the root to the search key.
# Return the json stringified list.
# The key is guaranteed to be in the tree.
def search(root: Node, search_key: int) -> str:
    curr = root
    list = [curr.key]

    while curr.key != search_key:
        if search_key > curr.key:
            curr = curr.rightchild
        else:
            curr = curr.leftchild

        list.append(curr.key)
        
    return(json.dumps(list))

def preorder_helper(root: Node):
    if root == None:
        return []

    list = [root.key]
    list.extend(preorder_helper(root.leftchild))
    list.extend(preorder_helper(root.rightchild))

    return list

# For the tree rooted at root, dump the preorder traversal to a stringified JSON list and return.
def preorder(root: Node) -> str:
    return(json.dumps(preorder_helper(root)))

def inorder_helper(root: Node):
    if root == None:
        return []

    list = []
    list.extend(inorder_helper(root.leftchild))
    list.append(root.key)
    list.extend(inorder_helper(root.rightchild))

    return list
    
# For the tree rooted at root, dump the inorder traversal to a stringified JSON list and return.
def inorder(root: Node) -> str:
    return(json.dumps(inorder_helper(root)))

def postorder_helper(root: Node):
    if root == None:
        return []

    list = []
    list.extend(postorder_helper(root.leftchild))
    list.extend(postorder_helper(root.rightchild))
    list.append(root.key)

    return list

# For the tree rooted at root, dump the postorder traversal to a stringified JSON list and return.
def postorder(root: Node) -> str:
    return(json.dumps(postorder_helper(root)))

# For the tree rooted at root, dump the BFT traversal to a stringified JSON list and return.
# The DFT should traverse left-to-right.
def bft(root: Node) -> str:
    list = []

    queue = [root]

    while queue:
        curr = queue.pop(0)
        list.append(curr.key)
        
        if curr.leftchild != None:
            queue.append(curr.leftchild)

        if curr.rightchild != None:
            queue.append(curr.rightchild)

    return json.dumps(list)    
