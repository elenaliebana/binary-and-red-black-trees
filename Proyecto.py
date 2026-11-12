import BinaryTree as BT
import RedBlackTree as RBT
import Opcional as op
import random
import sys
sys.setrecursionlimit(15000)

def read_words(letters, insertion:str):
    """
    Reads the words in the file and clasifies them in a binary tree and a red black tree

    Parameters:
    ----------
    letters: str
        initials for the words to clasify
    inrsetion: str
        insertion type (A / D)

    Returns:
    -------
    tuple[dict, dict]: tuple with both trees
    """
    word_dict = {}
    for letter in letters:
        word_dict[letter] = []

    with open("palabras_RAE_cleaned_noaccents.txt", "r", encoding = "utf-8") as file:
            for line in file:
                word = line.strip()
                start = word[0].lower()
                if start in word_dict:
                    word_dict[start].append(word)

    bin_trees = {}
    rb_trees = {}
    for letter in letters:
        bin_tree = BT.BinaryTree(None)
        rb_tree = RBT.RedBlackTree(None)
        word_list = word_dict[letter]

        if insertion == "A": # RANDOM INSERTION
            random.shuffle(word_list)

        for word in word_list:
            bin_tree.insert(word)
            rb_tree.insert(word)

        bin_trees[letter] = bin_tree
        rb_trees[letter] = rb_tree

    return bin_trees, rb_trees


if __name__ == "__main__":
    letters = []
    ok = True
    while ok:
        inp = input("Introduce las letras (hasta 3): ")
        for i in inp:
            if i.isalpha() and i != " ":
                if i not in letters: 
                    letters.append(i.lower())
        
        if 0 < len(letters) <= 3:
            ok = False
        else:
            print("Input inválido. Introduce de 1 a 3 letras.")
            letters = []

    insertion = ""
    while insertion.upper() != "D" and insertion.upper() != "A":
        insertion = input("Inserción por defecto o aleatoria (D / A): ").upper()

    bin_dict, rb_dict = read_words(letters, insertion)

    for letter in letters:
        t_bin = bin_dict[letter]
        t_rb = rb_dict[letter]
        
        print()
        print(f"="*40)
        print(f"ANÁLISIS PARA LA LETRA: '{letter.upper()}'")
        print(f"="*40)
        print()
        
        # BINARY SEARCH TREE
        print("ÁRBOL BINARIO DE BÚSQUEDA")
        if t_bin.root is not None:
            print(f"  - Raíz: {t_bin.root}")
            print(f"  - Hijo Izq Raíz: {t_bin.root.get_left()}")
            print(f"  - Hijo Der Raíz: {t_bin.root.get_right()}")
            print(f"  - Altura: {t_bin.height()}")
            print(f"  - Número de nodos: {t_bin.count_nodes_tree()}")
            print(f"  - Número de hojas: {t_bin.count_leafs()}")
            print(f"  - ¿Está inclinado?: {t_bin.skew()}")
            print(f"  - Ruta más larga: {t_bin.longest_path()}")
            print(f"  - Paths to leaf with length (4): {BT.paths_to_leaf_with_length(t_bin.root, 4, [], [])} ")
        else:
            print(f"No se han encontrado palabras para la letra {letter}")

        # RED-BLACK TREE
        print(f"\n[ÁRBOL ROJO-NEGRO]")
        if t_rb.root != t_rb.NIL:
            print(f"  - Raíz: {t_rb.root}")
            print(f"  - Hijo Izq Raíz: {t_rb.root.get_left()}")
            print(f"  - Hijo Der Raíz: {t_rb.root.get_right()}")
            print(f"  - Altura: {t_rb.height()}") 
            print(f"  - Número de nodos: {t_rb.count_nodes_tree()}")
            print(f"  - Número de hojas: {t_rb.count_leafs()}")
            print(f"  - ¿Está inclinado?: {t_rb.skew()}") 
            print(f"  - Ruta más larga: {t_rb.longest_path()}")
            print(f"  - Paths to leaf with length (4): {RBT.paths_to_leaf_with_length(t_rb.root, 4, [], [])} ")
        else:
            print(f"No se han encontrado palabras para la letra {letter}")

        print()
        print("-"*50)

        # GRAPH TREES
        # Esta función puede tardar mucho tiempo si el árbol tiene muchos nodos. 
        # Se recomienda utilizar las letras 'k', 'x' o 'w' para probarla.
        option = input(f"¿Deseas generar los plots para la letra '{letter.upper()}'?: ").upper()
        
        
        if option == "S":
            op.plot_bst(t_bin, letter)
            op.plot_rbt(t_rb, letter)
    
        # COMPARACIÓN
        height_diff = t_bin.height() - t_rb.height()
        print(f"El Árbol Rojo-Negro es más eficiente, reduciendo la altura en {height_diff} niveles respecto al BST.")
        print("Esto se debe a que el RBT realiza rotaciones para mantener el balanceo, evitando que")
        print("la estructura se alargue, especialmente cuando las palabras entran en orden alfabético.")