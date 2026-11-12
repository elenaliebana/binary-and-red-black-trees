from typing import List, Optional
import sys
sys.setrecursionlimit(15000)

class Node:
    def __init__(self, key, value=None):
        """
        Initializes a new Node with a key and an optional value.

        Parameters:
        ----------
        key : any
            Unique identifier for the node.
        value : any, optional
            Additional data associated with the node.
        """
        self._parent = None  # Pointer to the parent node
        self._left = None    # Pointer to the left child
        self._right = None   # Pointer to the right child
        self.key = key       # Key that identifies the node
        self.data = value    # Optional additional data

    def get_left(self) -> 'Node':
        """
        Retrieves the left child of the node.

        Returns:
        -------
        Node or None
        """
        return self._left

    def set_left(self, node) -> None:
        """
        Sets the left child of the node and updates the parent reference.

        Parameters:
        ----------
        node : Node
        """
        self._left = node
        if node is not None:
            node.set_parent(self)

    def get_right(self) -> 'Node':
        """
        Retrieves the right child of the node.

        Returns:
        -------
        Node or None
        """
        return self._right

    def set_right(self, node) -> None:
        """
        Sets the right child of the node and updates the parent reference.

        Parameters:
        ----------
        node : Node
        """
        self._right = node
        if node is not None:
            node.set_parent(self)

    def get_parent(self) -> 'Node':
        """
        Retrieves the parent of the node.

        Returns:
        -------
        Node or None
        """
        return self._parent

    def set_parent(self, node) -> None:
        """
        Sets the parent of the node.

        Parameters:
        ----------
        node : Node
        """
        self._parent = node

    def __str__(self):
        """
        Returns a string representation of the node (its key).
        """
        return f"{self.key}"

    def show(self, level=0, prefix="Root: ") -> None:
        """
        Displays the node and its children.

        Parameters:
        ----------
        level : int
            Current depth level.
        prefix : str
            Label to identify root, left, or right children.
        """
        indent = " " * (level * 4)
        print(f"{indent}{prefix}{self}")

        if self.get_left() is not None:
            self.get_left().show(level + 1, prefix="L--- ")
        if self.get_right() is not None:
            self.get_right().show(level + 1, prefix="R--- ")

    def min_key(self):
        """
        Finds the node with the minimum key in the tree.

        Returns:
        -------
        Node
        """
        current = self
        while current.get_left() is not None:
            current = current.get_left()
        
        return current

    def max_key(self):
        """
        Finds the node with the maximum key in the tree.

        Returns:
        -------
        Node
        """
        current = self
        while current.get_right() is not None:
            current = current.get_right()
        
        return current
    
    def find_node(self, key):
        """
        Searches for a node by its key.

        Parameters:
        ----------
        key : any
            The key to search for.

        Returns:
        -------
        Node or None
        """
        if self.key == key:
            return key, self.data
        
        elif self.key > key and self.get_left() is not None:
            return self.get_left().find_node(key)
        
        elif self.key < key and self.get_right() is not None:
            return self.get_right().find_node(key)
        
        return None
          
    def predecessor(self):
        """
        Finds the predecessor of the current node.

        Returns:
        -------
        Node or None
        """
        if self.get_left() is not None:
            return self.get_left().max_key()
        current = self
        parent = self.get_parent()
        while parent is not None and current == parent.get_left():
            current = parent
            parent = parent.get_parent()
        return parent
    
    def successor(self):
        """
        Finds the successor of the current node.

        Returns:
        -------
        Node or None
        """
        if self.get_right() is not None:
            return self.get_right().min_key()
        current = self
        parent = self.get_parent()
        while parent is not None and current == parent.get_right():
            current = parent
            parent = parent.get_parent()
        return parent
    
    def node_clone(self):
        """
        Creates a copy of the current node without its connections.

        Returns:
        -------
        Node
        """
        return Node(self.key, self.data)
     

class BinaryTree:
    def __init__(self, root: Node):
        """
        Initializes the binary tree with a root node.

        Parameters:
        ----------
        root : Node
            The root node of the binary tree.
        """
        self.root = root

    def show(self) -> None:
        """Displays the entire binary tree."""
        self.root.show()
        

    def insert(self, key, value=None):
        """
        Inserts a new key into the binary search tree.

        Parameters:
        ----------
        key : any
            Key to be inserted.
        value : 
            Additional data associated with the node
        """
        new_node = Node(key, value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            cond = True
            while cond:
                if key < current.key:
                    if current.get_left() is None:
                        current.set_left(new_node)
                        cond = False
                    else:
                        current = current.get_left()

                else:
                    if current.get_right() is None:
                        current.set_right(new_node)
                        cond = False
                    else:
                        current = current.get_right()

    def delete(self, key):
        """
        Deletes a node from the tree based on its key.

        Parameters:
        ----------
        key : any
            The key of the node to delete.
        """
        if self.root == None: 
            return
        
        current = self.root
        while current is not None and current.key is not key:
            if key < current.key:
                current = current.get_left()
            else:
                current = current.get_right()

        if current == None: 
            return 
        
        # CASO 1: HOJA
        elif current.get_left() is None and current.get_right() is None:
            if current == self.root:
                self.root = None

            else:
                parent = current.get_parent()
                if current == parent.get_left():
                    parent.set_left(None)
                else:
                    parent.set_right(None)


        # CASO 2: 1 HIJO
        elif current.get_left() is None or current.get_right() is None:
            if current.get_left() is not None:
                child = current.get_left()
            else:
                child = current.get_right()

            if current == self.root:
                self.root = child
                child.set_parent(None)

            else:
                parent = current.get_parent()
                child.set_parent(parent)
                if current == parent.get_left():
                    parent.set_left(child)
                else:
                    parent.set_right(child)

        # CASO 3: 2 HIJOS
        else: 
            suc = current.successor()
            temp = suc.node_clone()
            suc_parent = suc.get_parent()
            suc_child = suc.get_right() # El sucesor no tiene hijo izquierdo

            if suc_child is not None:
                suc_child.set_parent(suc_parent)

            if suc == suc_parent.get_left():
                suc_parent.set_left(suc_child) 
            else:
                suc_parent.set_right(suc_child) 

            swap_contents(current, temp)    
   
    def height(self) -> None: # 0 INDEX
        """
        Calculates the height of the tree.

        Returns:
        -------
        int
            number of branches
        """
        if self.root == None:
            return -1

        left_height = BinaryTree(self.root.get_left()).height()
        right_height = BinaryTree(self.root.get_right()).height()

        return 1 + max(left_height, right_height)  
    
    def skew(self) -> bool:
        """
        Checks if the tree is unbalanced.

        Returns:
        -------
        bool
            True if any subtree has a balance factor outside [-1, 0, 1].
        """
        if self.root is None:
            return False

        left_height = BinaryTree(self.root.get_left()).height()
        right_height = BinaryTree(self.root.get_right()).height()

        balance = right_height - left_height
        
        if balance not in [-1, 0, 1]:
            root_skew = True
        else:
            root_skew = False
        
        return root_skew or BinaryTree(self.root.get_left()).skew() or BinaryTree(self.root.get_right()).skew()
    

    # 3. LECTURA DE PALABRAS

    def count_nodes_tree(self) -> int:
        """
        Counts the total number of nodes in the tree.

        Returns:
        -------
        int
        """
        if self.root is None:
            return 0
        return 1 + BinaryTree(self.root.get_left()).count_nodes_tree() + BinaryTree(self.root.get_right()).count_nodes_tree()

    def count_leafs(self) -> int:
        """
        Counts the total number of leaf nodes in the tree.

        Returns:
        -------
        int
        """
        if self.root is None:
            return 0
       
        if self.root.get_left() is None and self.root.get_right() is None:
            return 1

        return BinaryTree(self.root.get_left()).count_leafs() + BinaryTree(self.root.get_right()).count_leafs()
    
    def longest_path(self) -> list:
        """
        Finds the longest path from the root to a leaf.

        Returns:
        -------
        list
            A list of keys representing the path.
        """
        if self.root is None:
            return []
        
        left_path = BinaryTree(self.root.get_left()).longest_path()
        right_path = BinaryTree(self.root.get_right()).longest_path()

        if len(left_path) > len(right_path):
            return [self.root.key] + left_path
        else:
            return [self.root.key] + right_path
       

# 2.1. IMPRIMIR ÁRBOL

def swap_contents(node1:Node, node2:Node) -> None:
    """
    Swaps the key and data between two nodes.

    Parameters:
    ----------
    node1 : Node
    node2 : Node
    """
    node1.key = node2.key
    node1.data = node2.data
    return

class Queue:
    """
    Class representing a circular queue with a size limit.

    Attributes:
    -----------
    head : int
        Index of the front element in the queue.
    tail : int
        Index of the last element in the queue.
    """

    def __init__(self, length: int):
        """
        Initializes an empty circular queue with a maximum capacity.

        Parameters:
        -----------
        length : int
            The maximum capacity of the circular queue.
        """
        self.array = [None] * length  # Redefine items to match the circular queue
        self.head = self.tail = -1
        self.length = length

    def __str__(self):
        """
        Prints the elements of the queue
        """
        s = ""
        for i in self.array:
            if i is not None:
                s += str(i) + " -> "
        return s

    def size(self) -> int:
        """
        Calculates the  number of elements in the queue.

        Returns:
        -------
        int
        """
        if self.is_empty():
            return 0
        elif self.tail >= self.head:
            return self.tail - self.head + 1
        else:
            return self.length - (self.head - self.tail - 1)

    def is_full(self) -> bool:
        """
        Checks if the circular queue is full.

        Returns:
        --------
        bool
            True if the circular queue is full, False otherwise.
        """
        if self.is_empty():
            return False  # An empty queue cannot be full
        return (self.tail + 1) % self.length == self.head
    
    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        Returns:
        --------
        bool
            True if the queue is empty, False otherwise.
        """
        return self.head == -1 and self.tail == -1

    def enqueue(self, item):
        """
        Adds an element to the circular queue if it is not full.

        Parameters:
        -----------
        item : any type
            The element to add to the circular queue.
        """
        if self.is_full():
            print("Queue is full")
        elif self.head == -1:  # Empty queue
            self.head = self.tail = 0
            self.array[self.tail] = item
        else:
            self.tail = (self.tail + 1) % self.length
            self.array[self.tail] = item

    def dequeue(self):
        """
        Removes and returns the front element of the circular queue.

        Returns:
        --------
        any type
            The front element of the circular queue if it is not empty, None otherwise.
        """
        if self.is_empty():
            print("Queue is empty")
            return None
        elif self.head == self.tail:  # Only one element in the queue
            temp = self.array[self.head]
            self.array[self.head] = None
            self.head = self.tail = -1
            return temp
        else:
            temp = self.array[self.head]
            self.array[self.head] = None
            self.head = (self.head + 1) % self.length
            return temp

    def show(self):
        """
        Displays the elements of the circular queue in order.
        """
        if self.is_empty():
            print("Queue is empty")
        elif self.tail >= self.head:
            for i in range(self.head, self.tail + 1):
                print(self.array[i], end = " ")
        else:
            for i in range(self.head, self.length):
                print(self.array[i], end = " ")
            for i in range(0, self.tail + 1):
                print(self.array[i], end = " ")

def in_order(tree: BinaryTree) -> None:
    """
    Prints in-order (Left, Root, Right).

    Parameters:
    ----------
    tree : BinaryTree
    """
    if tree is not None and tree.root is not None:
        in_order(BinaryTree(tree.root.get_left()))
        print(tree.root.key)
        in_order(BinaryTree(tree.root.get_right()))    

def pre_order(tree: BinaryTree) ->None:
    """
    Prints pre-order (Root, Left, Right).

    Parameters:
    ----------
    tree : BinaryTree
    """
    if tree is not None and tree.root is not None:
        print(tree.root.key)
        pre_order(BinaryTree(tree.root.get_left()))
        pre_order(BinaryTree(tree.root.get_right()))

def post_order(tree: BinaryTree) ->None:
    """
    Prints post-order (Left, Right, Root).

    Parameters:
    ----------
    tree : BinaryTree
    """
    if tree is not None and tree.root is not None:
        post_order(BinaryTree(tree.root.get_left()))
        post_order(BinaryTree(tree.root.get_right()))
        print(tree.root.key)

def level_order(tree: BinaryTree) -> None:
    """
    Prints level-order.

    Parameters:
    ----------
    tree : BinaryTree
    """
    if tree.root is None:
        return
    
    q = Queue(tree.count_nodes_tree())
    q.enqueue(tree.root)
    
    while not q.is_empty():
        node = q.dequeue()
        print(node.key)
        if node.get_left() is not None:
            q.enqueue(node.get_left())
        if node.get_right() is not None:
            q.enqueue(node.get_right())


def paths_to_leaf_with_length(
    node: Optional["Node"],
    remaining_edges: int,
    current_path: Optional[List[str]] =None,
    results: Optional[List[List[str]]] =None,
    ) ->List[List[str]]:

    """
    Devuelve todos los caminos raiz->hoja con longitud exacta (en
    aristas) igual a remaining_edges al comienzo de la llamada.

    Uso tipico:
    paths = paths_to_leaf_with_length(tree.root, 3)

    Parametros:
    - node: nodo actual (comienza en la raiz)
    - remaining_edges: cuantas aristas faltan para alcanzar la longitud objetivo
    - current_path: (interno) lista con el camino actual
    - results: (interno) acumulador de caminos validos

    Retorna:
    - Lista de caminos; cada camino es una lista de strings (str(node.key)).

    """

    if current_path is None:
        current_path = []

    if results is None:
        results = []

    if node is None:
        return results

    current_path.append(str(node.key))

    if node.get_left() is None and node.get_right() is None:
        if remaining_edges == 0:
            results.append(list(current_path))

    else:
        if remaining_edges > 0:
            if node.get_left() is not None:
                paths_to_leaf_with_length(node.get_left(), remaining_edges - 1, current_path, results)

            if node.get_right() is not None:
                paths_to_leaf_with_length(node.get_right(), remaining_edges - 1, current_path, results)

    current_path.pop()
    return results

if __name__ == "__main__": 
    # CREACIÓN DEL ÁRBOL
    tree = BinaryTree(Node(50)) 

    tree.insert(30)
    tree.insert(40)

    tree.insert(70)
    tree.insert(60)
    tree.insert(80)
    tree.insert(90)
    tree.insert(100)

    print("TREE:")
    tree.show()
    print("-" * 40)

    # MÉTRICAS
    print(f"Height (expected - 4): {tree.height()}")
    print(f"Skew (expected - True): {tree.skew()}") 
    print(f"Number of nodes (expected - 8): {tree.count_nodes_tree()}") 
    print(f"Number of leafs (expected - 3): {tree.count_leafs()}")
    print(f"Longest path (expected - [50, 70, 80, 90, 100]): {tree.longest_path()}")
    print(f"Find node (expected - (90, None)): {tree.root.find_node(90)}")
    print("-" * 40)

    # IMPRIMIR
    print("In-order (expected - 30 40 50 60 70 80 90 100)")
    in_order(tree)
    
    print("Pre-order (expected - 50 30 40 70 60 80 90 100)")
    pre_order(tree)
    
    print("Post-order (expected - 40 30 60 100 90 80 70 50)") 
    post_order(tree)
    
    print("Level-order (expected - 50 30 70 40 60 80 90 100)")
    level_order(tree)
    print("-" * 40)

    # ELIMINAR
    print("Delete (80)")
    tree.delete(80) 
    tree.show()
    
    print("Delete (40)")
    tree.delete(30) 
    tree.show()

    print("Delete (100)")
    tree.delete(100) 
    tree.show()

    # PATHS TO LEAF
    print()
    print("-"*40)
    print("Paths to leaf")
    paths1= paths_to_leaf_with_length(tree.root, 1, [], [])
    print(f"Longitud 1 (expected - [50, 40]): {paths1}") 

    paths2 = paths_to_leaf_with_length(tree.root, 2, [], [])
    print(f"Longitud 2 (expected - [[50, 70, 60], [50, 70, 90]]): {paths2}")
    