

class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
    ### additional methods ###
    def get_key(self):
        return self.key
    def get_value(self):
        return self.value
        

class BinarySearchTree:

    # Constructor just assigns an empty root.
    def __init__(self):
        self.root = None


    # Search for a node containing a matching key. Returns the
    # Node object that has the matching key if found, None if
    # not found.
    def search(self, desired_key):
        current_node = self.root
        while current_node is not None:
            # Return the node if the key matches.
            if current_node.key == desired_key:
                return current_node
            # Navigate to the left if the search key is
            # less than the node's key.
            elif desired_key < current_node.key:
                current_node = current_node.left
            # Navigate to the right if the search key is
            # greater than the node's key.
            else:
                current_node = current_node.right
        # The key was not found in the tree.
        return None


    # Inserts the new node into the tree.
    def insert(self, node):

        # Check if the tree is empty
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None: 
                if node.key < current_node.key:
                    # If there is no left child, add the new
                    # node here; otherwise repeat from the
                    # left child.
                    if current_node.left is None:
                        current_node.left = node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    # If there is no right child, add the new
                    # node here; otherwise repeat from the
                    # right child.
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right       


    # Removes the node with the matching key from the tree.
    # f this method and that it didn't work right out the box
    # f it right in the a
    def remove(self, key):
        parent = None
        current_node = self.root
        while current_node is not None:
            if current_node.key == key:
                if current_node.left is None and current_node.right is None:
                    if parent is None:self.root = None
                    elif parent.left is current_node:parent.left = None
                    else:parent.right = None
                    return
                elif current_node.left is None:
                    if parent is None:self.root = current_node.right
                    elif parent.left is current_node:parent.left = current_node.right
                    else:parent.right = current_node.right
                    return
                elif current_node.right is None:
                    if parent is None:self.root = current_node.left
                    elif parent.left is current_node:parent.left = current_node.left
                    else:parent.right = current_node.left
                    return
                else:
                    successor = current_node.right
                    successor_parent = current_node
                    while successor.left is not None:
                        successor_parent = successor
                        successor = successor.left
                    current_node.key = successor.key
                    current_node.value = successor.value
                    if successor_parent.left == successor:
                        successor_parent.left = successor.right
                    else:successor_parent.right = successor.right
                    return
            elif current_node.key < key:
                parent = current_node
                current_node = current_node.right
            else:
                parent = current_node
                current_node = current_node.left
        print(f"Key {key} not found in the tree.")
        return None 



        ####### ADDITIONAL METHODS #######
    def inorder_traversal(self, node):
        return_list = []                                    # a list to hold all nodes in order
        if node is not None:                                        # recursively search all nodes
            return_list.extend(self.inorder_traversal(node.left))   # searches all left first
            return_list.append(node.key)                            # add node to return list
            return_list.extend(self.inorder_traversal(node.right))  # search all right next
        return return_list                                          # return that list

    def preorder_traversal(self,node):
        return_list = []
        if node is not None:
            return_list.append(node.key)                            # append first
            return_list.extend(self.preorder_traversal(node.left))  # then do left
            return_list.extend(self.preorder_traversal(node.right)) # then do right
        return return_list

    def postorder_traversal(self,node):
        return_list = []
        if node is not None:
            return_list.append(node.key)                            # append first
            return_list.extend(self.postorder_traversal(node.right))# then do right
            return_list.extend(self.postorder_traversal(node.left)) # then do left
        return return_list
    
    ### additional methods ###

    def get_keys_value(self, key):
        node = self.search(key)
        
        if node is not None:
            return node.get_value()
        else:
            return None
        
    def print_keys_value(self, key):
        node = self.search(key)
        
        if node is not None:
            return node.get_value()
        else:
            return None