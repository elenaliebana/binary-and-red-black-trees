from typing import List, Optional
from enum import Enum
import sys
sys.setrecursionlimit(15000)

class Color(Enum):
    RED = 0 
    BLACK = 1

class RBNode:
    def __init__(self, key, value=None, color=Color.RED):
        self._parent = None
        self._left = None
        self._right = None
        self.key = key
        self.data = value
        self.color = color

    def is_red(self) -> bool:
        """
        Checks if the node is red.
        """
        return self.color == Color.RED

    def is_black(self) -> bool:
        """
        Checks if the node is black.
        """
        return self.color == Color.BLACK

    def set_red(self) -> None:
        """
        Sets the node color to red.
        """
        self.color = Color.RED

    def set_black(self) -> None:
        """
        Sets the node color to black.
        """
        self.color = Color.BLACK

    def get_left(self) -> 'RBNode':
        """
        Gets the left child node.
        """
        return self._left

    def set_left(self, node) -> None:
        """
        Sets the left child node.
        """
        self._left = node

    def get_right(self) -> 'RBNode':
        """
        Gets the right child node.
        """
        return self._right

    def set_right(self, node) -> None:
        """
        Sets the right child node.
        """
        self._right = node

    def get_parent(self) -> 'RBNode':
        """
        Gets the parent node.
        """
        return self._parent

    def set_parent(self, node) -> None:
        """
        Sets the parent node.
        """
        self._parent = node

    def __str__(self):
        """
        Prints nodes
        """
        color_str = "R" if self.is_red() else "B"
        return f"{self.key} ({color_str})"
    
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
        if self.key is None:
            return
        indent = " " * (level * 4)
        print(f"{indent}{prefix}{self}")

        if self.get_left() is not None and self.get_left().get_left() is not None:
            self.get_left().show(level + 1, prefix="L--- ")
        if self.get_right() is not None and self.get_right().get_right() is not None:
            self.get_right().show(level + 1, prefix="R--- ")

    def min_key(self, nil):
        """
        Finds the node with the minimum key in the tree.

        Arguments:
        -------
        nil: tree's NIL node

        Returns:
        -------
        RBNode
        """
        current = self
        while current.get_left() is not nil:
            current = current.get_left()
        
        return current

    def max_key(self, nil):
        """
        Finds the node with the maximum key in the tree.

        Arguments:
        -------
        nil: tree's NIL node

        Returns:
        -------
        RBNode
        """
        current = self
        while current.get_right() is not nil:
            current = current.get_right()
        
        return current

    def predecessor(self, nil):
        """
        Finds the predecessor of the current node.

        Arguments:
        -------
        nil: tree's NIL node

        Returns:
        -------
        RBNode
        """
        if self.get_left() is not nil:
            return self.get_left().max_key()
        current = self
        parent = self.get_parent()
        while parent is not nil and current == parent.get_left():
            current = parent
            parent = parent.get_parent()
        return parent
    
    def successor(self, nil):
        """
        Finds the successor of the current node.

        Arguments:
        -------
        nil: tree's NIL node

        Returns:
        -------
        RBNode
        """
        if self.get_right() is not nil:
            return self.get_right().min_key(nil)
        current = self
        parent = self.get_parent()
        while parent is not nil and current == parent.get_right():
            current = parent
            parent = parent.get_parent()
        return parent
    
    def find_node(self, key):
        """
        Searches for a node by its key.

        Parameters:
        ----------
        key : any
            The key to search for.

        Returns:
        -------
        Tuple (key, value)
        """
    
        if self.key is None:
            return None
        
        if self.key == key:
            return key, self.data
        
        elif self.key > key and self.get_left().key is not None:
            return self.get_left().find_node(key)
        
        elif self.key < key and self.get_right().key is not None:
            return self.get_right().find_node(key)
        
        return None

    def find_node_v2(self, key): # For the delete function. Returns a Node instead of a tuple.
        """
        Searches for a node by its key.

        Parameters:
        ----------
        key : any
            The key to search for.

        Returns:
        -------
        Node
        """
    
        if self.key is None:
            return None
        
        if self.key == key:
            return self
        
        elif self.key > key and self.get_left().key is not None:
            return self.get_left().find_node_v2(key)
        
        elif self.key < key and self.get_right().key is not None:
            return self.get_right().find_node_v2(key)
        
        return None

class RedBlackTree :
    def __init__ (self, root:RBNode = None):
        """
        Initializes a Red-Black Tree.

        Parameters:
        ----------
        root : RBNode
            Initial root node for the tree.
        """
        self.NIL = RBNode(None, color=Color.BLACK)
        self.NIL.set_left(self.NIL)
        self.NIL.set_right(self.NIL)
        self.NIL.set_parent(self.NIL)
        self.root = self.NIL

        self.root = self.NIL
        if root is not None:
            self.root = root

    def left_rotation(self, x:RBNode):
        """
        Performs a left rotation around node x to adjust balance.

        Parameters:
        ----------
        x : RBNode
            The pivot node for the rotation.
        """
        y = x.get_right()  
        x.set_right(y.get_left())  
        if y.get_left() != self.NIL:
            y.get_left().set_parent(x)  

        y.set_parent(x.get_parent())  
        if x.get_parent() == self.NIL: 
            self.root = y
        elif x == x.get_parent().get_left(): 
            x.get_parent().set_left(y)
        else:  
            x.get_parent().set_right(y)

        y.set_left(x)  
        x.set_parent(y)
    
    def right_rotation(self,y:RBNode):
        """
        Performs a right rotation around node y to adjust balance.

        Parameters:
        ----------
        y : RBNode
            The pivot node for the rotation.
        """
        x = y.get_left()
        y.set_left(x.get_right())

        if x.get_right() != self.NIL:
            x.get_right().set_parent(y)
        
        x.set_parent(y.get_parent())

        if y.get_parent() == self.NIL:
            self.root = x
        elif y == y.get_parent().get_left():
            y.get_parent().set_left(x)
        else:
            y.get_parent().set_right(x)

        x.set_right(y)
        y.set_parent(x)

        return
    
    def insert(self, key, value=None):
        """
        Inserts a new key into the tree.

        Parameters:
        ----------
        key : any
            The key to insert.
        value : 
            Associated data.
        """
        z = RBNode(key, value, color = Color.RED)
        z.set_left(self.NIL)
        z.set_right(self.NIL)
        z.set_parent(self.NIL)

        y = self.NIL
        x = self.root

        while x != self.NIL:
            y = x
            if z.key < x.key: 
                x = x.get_left()
            else:
                x = x.get_right()
        
        z.set_parent(y)

        if y == self.NIL:
            self.root = z
        elif z.key < y.key:
            y.set_left(z)
        else:
            y.set_right(z)

        z.set_red()
        self.insert_fixup(z)

    def insert_fixup(self , z:RBNode):
        """
        Restores Red-Black properties after a new node is inserted.

        Parameters:
        ----------
        z : RBNode
            The node to check.
        """
        while z.get_parent() != self.NIL and z.get_parent().is_red():
            if z.get_parent() == z.get_parent().get_parent().get_left():
                y = z.get_parent().get_parent().get_right() # y = uncle

                # CASE 1: UNCLE IS RED
                if y.is_red():
                    z.get_parent().set_black()
                    y.set_black()
                    z.get_parent().get_parent().set_red()
                    z = z.get_parent().get_parent()
                
                # CASE 2: Z IS RIGHT CHILD
                else:
                    if z == z.get_parent().get_right():
                        z = z.get_parent()
                        self.left_rotation(z)

                    z.get_parent().set_black()
                    z.get_parent().get_parent().set_red()
                    self.right_rotation(z.get_parent().get_parent())
            
            else:
                y = z.get_parent().get_parent().get_left() # y = uncle

                # CASE 1: UNCLE IS RED
                if y.is_red():
                    z.get_parent().set_black()
                    y.set_black()
                    z.get_parent().get_parent().set_red()
                    z = z.get_parent().get_parent()
                
                # CASE 2: Z IS RIGHT CHILD
                else:
                    if z == z.get_parent().get_left():
                        z = z.get_parent()
                        self.right_rotation(z)

                    z.get_parent().set_black()
                    z.get_parent().get_parent().set_red()
                    self.left_rotation(z.get_parent().get_parent())

        self.root.set_black()

    def transplant(self, u:RBNode, v:RBNode):
        """
        Replaces one subtree with another.

        Parameters:
        ----------
        u : RBNode
            Subtree to be replaced.
        v : RBNode
            Replacement subtree.
        """
        if u.get_parent() == self.NIL:
            self.root = v
        elif u == u.get_parent().get_left():
            u.get_parent().set_left(v)
        else:
           u.get_parent().set_right(v)

        v.set_parent(u.get_parent())

    def delete(self, key):
        """
        Removes a node from the tree.

        Parameters:
        ----------
        key: int
            Key of the node to be deleted.
        """
        z = self.root.find_node_v2(key)
        if z is None or z == self.NIL:
            print(f"La clave {key} no existe.")
            return  
        y = z
        y_original_color = y.color
        if z.get_left() == self.NIL:
            x = z.get_right()
            self.transplant(z, z.get_right())

        elif z.get_right() == self.NIL:
            x = z.get_left()
            self.transplant(z, z.get_left())

        else:
            y = z.successor(self.NIL)
            y_original_color = y.color
            x = y.get_right()
            if y != z.get_right():
                self.transplant(y, y.get_right())
                y.set_right(z.get_right())
                y.get_right().set_parent(y)
            else:
                x.set_parent(y)

            self.transplant(z, y)
            y.set_left(z.get_left())
            y.get_left().set_parent(y)
            y.color = z.color

        if y_original_color == Color.BLACK:
            self.delete_fixup(x)

    def delete_fixup(self, x:RBNode):
        """
        Restores Red-Black properties after a new node is deleted.

        Parameters:
        ----------
        x : RBNode
            The node to check.
        """
        while x != self.root and x.is_black():
            if x == x.get_parent().get_left():
                w = x.get_parent().get_right() # w = sibling

                # CASE 1: W IS RED
                if w.is_red():
                    w.set_black()
                    x.get_parent().set_red()
                    self.left_rotation(x.get_parent())
                    w = x.get_parent().get_right()

                # CASE 2: W IS BLACK WITH 2 BLACK CHILDREN
                elif w.get_left().is_black() and w.get_right().is_black():
                    w.set_red()
                    x = x.get_parent()

                # CASE 3: W IS BLACK WITH LEFT RED AND RIGHT BLACK 
                else:
                    if w.get_right().is_black():
                        w.get_left().set_black()
                        w.set_red()
                        self.right_rotation(w)
                        w = x.get_parent().get_right()

                    # CASE 4: W IS BLACK WITH RIGHT RED
                    w.color = x.get_parent().color
                    x.get_parent().set_black()
                    w.get_right().set_black()
                    self.left_rotation(x.get_parent())
                    x = self.root

            else:
                w = x.get_parent().get_left() # w = sibling

                # CASE 1: W IS RED
                if w.is_red():
                    w.set_black()
                    x.get_parent().set_red()
                    self.right_rotation(x.get_parent())
                    w = x.get_parent().get_left()

                # CASE 2: W IS BLACK WITH 2 BLACK CHILDREN
                elif w.get_right().is_black() and w.get_left().is_black():
                    w.set_red()
                    x = x.get_parent()

                # CASE 3: W IS BLACK WITH LEFT RED AND RIGHT BLACK 
                else:
                    if w.get_left().is_black():
                        w.get_right().set_black()
                        w.set_red()
                        self.left_rotation(w)
                        w = x.get_parent().get_left()

                    # CASE 4: W IS BLACK WITH RIGHT RED
                    w.color = x.get_parent().color
                    x.get_parent().set_black()
                    w.get_left().set_black()
                    self.right_rotation(x.get_parent())
                    x = self.root
        x.set_black() 
    def height(self)-> int:
        """
        Finds the height of the tree
       
        Returns: 
        -------
            int: the height of the tree
        """

        node = self.root

        if node is self.NIL or node.key is None:
            return -1
        
        left_tree = RedBlackTree(self.root.get_left())
        left_tree.NIL = self.NIL
        
        right_tree = RedBlackTree(self.root.get_right())
        right_tree.NIL = self.NIL

        left_height = left_tree.height()
        right_height = right_tree.height()
       
        return 1 + max(left_height, right_height)
   
    def skew(self) -> bool:
        """
        Checks if the tree is unbalanced.

        Returns:
        -------
        bool
            True if any subtree has a balance factor outside [-1, 0, 1].
        """

        if self.root is self.NIL or self.root.key is None:
            return False
       
        left_tree = RedBlackTree(self.root.get_left())
        left_tree.NIL = self.NIL
        
        right_tree = RedBlackTree(self.root.get_right())
        right_tree.NIL = self.NIL

        left_height = left_tree.height()
        right_height = right_tree.height()

        balance = right_height - left_height

        left_skew = left_tree.skew()
        right_skew = right_tree.skew()

        if balance not in [-1, 0, 1]:
            root_skew = True
        else:
            root_skew = False

        return root_skew or left_skew or right_skew
    
    def count_nodes_tree(self) -> int:
        """
        Counts the total number of nodes in the tree.

        Returns:
        -------
        int
        """
        if self.root is self.NIL:
            return 0
        
        left_tree = RedBlackTree(self.root.get_left())
        left_tree.NIL = self.NIL
        
        right_tree = RedBlackTree(self.root.get_right())
        right_tree.NIL = self.NIL
        
        return 1 + left_tree.count_nodes_tree() + right_tree.count_nodes_tree()

    def count_leafs(self) -> int:
        """
        Counts the total number of leaf nodes in the tree.

        Returns:
        -------
        int
        """
        if self.root is self.NIL:
            return 0
       
        if self.root.get_left() is self.NIL and self.root.get_right() is self.NIL:
            return 1

        left_tree = RedBlackTree(self.root.get_left())
        left_tree.NIL = self.NIL 
        
        right_tree = RedBlackTree(self.root.get_right())
        right_tree.NIL = self.NIL 

        return left_tree.count_leafs() + right_tree.count_leafs()
    
    def longest_path(self) -> list:
        """
        Finds the longest path from the root to a leaf.

        Returns:
        -------
        list
            A list of keys representing the path.
        """
        if self.root is self.NIL:
            return []
        
        left_tree = RedBlackTree(self.root.get_left())
        left_tree.NIL = self.NIL 
        
        right_tree = RedBlackTree(self.root.get_right())
        right_tree.NIL = self.NIL
        
        left_path = left_tree.longest_path()
        right_path = right_tree.longest_path()

        if len(left_path) > len(right_path):
            return [self.root.key] + left_path
        else:
            return [self.root.key] + right_path
       

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


def swap_contents(node1:RBNode, node2:RBNode) -> None:
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

def in_order(tree: RedBlackTree) -> None:
    """
    Prints in-order (Left, Root, Right).

    Parameters:
    ----------
    tree : RedBlackTree
    """
    if tree is not None and tree.root is not tree.NIL:
        left = RedBlackTree(tree.root.get_left())
        left.NIL = tree.NIL
        right = RedBlackTree(tree.root.get_right())
        right.NIL = tree.NIL
        in_order(left) 
        print(tree.root.key)
        in_order(right)  

def pre_order(tree: RedBlackTree) -> None:
    """
    Prints pre-order (Root, Left, Right).

    Parameters:
    ----------
    tree : RedBlackTree
    """
    if tree is not None and tree.root is not tree.NIL:
        left = RedBlackTree(tree.root.get_left())
        left.NIL = tree.NIL
        right = RedBlackTree(tree.root.get_right())
        right.NIL = tree.NIL
        print(tree.root.key)
        pre_order(left) 
        pre_order(right)  

def post_order(tree: RedBlackTree) -> None:
    """
    Prints post-order (Left, Right, Root).

    Parameters:
    ----------
    tree : RedBlackTree
    """
    if tree is not None and tree.root is not tree.NIL:
        left = RedBlackTree(tree.root.get_left())
        left.NIL = tree.NIL
        right = RedBlackTree(tree.root.get_right())
        right.NIL = tree.NIL
        print(tree.root.key)
        post_order(left) 
        post_order(right)  

def level_order(tree: RedBlackTree) -> None:
    """
    Prints level-order.

    Parameters:
    ----------
    tree : RedBlackTree
    """
    if tree.root is tree.NIL:
        return
    
    q = Queue(tree.count_nodes_tree())
    q.enqueue(tree.root)
    
    while not q.is_empty():
        node = q.dequeue()
        print(node.key)
        if node.get_left() is not tree.NIL:
            q.enqueue(node.get_left())
        if node.get_right() is not tree.NIL:
            q.enqueue(node.get_right())

def paths_to_leaf_with_length(
    node: Optional["RBNode"],
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

    if node is None or node.key is None:
        return results

    current_path.append(str(node.key))

    if node.get_left().key is None and node.get_right().key is None:
        if remaining_edges == 0:
            results.append(list(current_path))

    else:
        if remaining_edges > 0:
            if node.get_left().key is not None:
                paths_to_leaf_with_length(node.get_left(), remaining_edges - 1, current_path, results)

            if node.get_right().key is not None:
                paths_to_leaf_with_length(node.get_right(), remaining_edges - 1, current_path, results)

    current_path.pop()
    return results

if __name__ == "__main__":
    rbt = RedBlackTree() 
    elementos = [50, 30, 40, 70, 60, 80, 90, 100]
    for num in elementos:
        rbt.insert(num)

    print("RED-BLACK TREE:")
    rbt.root.show() 
    print("-" * 40)

    # MÉTRICAS
    print(f"Height (expected - 3): {rbt.height()}")
    print(f"Skew (expected - False): {rbt.skew()}") 
    print(f"Number of nodes (expected - 8): {rbt.count_nodes_tree()}") 
    print(f"Number of leafs (expected - 4): {rbt.count_leafs()}")
    print(f"Longest path (expected - [60, 80, 90, 100]): {rbt.longest_path()}")
    print(f"Find node (expected - (90, None)): {rbt.root.find_node(90)}")

    # IMPRIMIR
    print("In-order (expected - 30 40 50 60 70 80 90 100):")
    in_order(rbt)
    
    print("Pre-order (expected - 60 40 30 50 80 70 90 100):")
    pre_order(rbt)
    
    print("Post-order (expected - 60 40 30 50 80 70 90 100):") 
    post_order(rbt)
    
    print("Level-order (expected - 60 40 80 30 50 70 90 100):")
    level_order(rbt)
    print("-" * 40)

    # ELIMINACIÓN
    print("Delete (90)")
    rbt.delete(90) 
    rbt.root.show() 
    
    print("Delete (40)")
    rbt.delete(40) 
    rbt.root.show() 

    # PATHS TO LEAF
    print()
    print("Paths to leaf")
    caminos2 = paths_to_leaf_with_length(rbt.root, 2)
    print(f"Longitud 2 (expected - [[60, 50, 30], [60, 80, 70], [60, 80, 100]]): {caminos2}")
    