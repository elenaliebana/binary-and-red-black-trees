import matplotlib.pyplot as plt # Utilizo la librería matplotlib

def plot_bst(tree, letter):
    """
    Genera una visualización gráfica de un Árbol Binario de Búsqueda.

    Parámetros:
    - tree: Árbol binario a graficar
    - letter: String con la letra analizada (para el título del gráfico).

    Retorna:
    - None: Muestra el gráfico.
    """

    if tree.root is None:
        return
    
    plt.figure(figsize=(10, 6))
    plt.title(f"BST - Letra {letter.upper()}")

    dibujar_bst(tree.root, 0, 0, 4)
    plt.show()

def dibujar_bst(node, x, y, espaciado):
    """
    Posiciona y pinta los nodos del árbol binario

    Parámetros:
    - node: Nodo actual a dibujar.
    - x, y: Coordenadas en el plano
    - espaciado: Distancia horizontal para separar los hijos
    """
    if node is None:
        return
    
    if node.get_left() is not None:
        plt.plot([x, x - espaciado], [y, y - 1], color='black') # Dibuja la arista
        dibujar_bst(node.get_left(), x - espaciado, y - 1, espaciado / 2) # Recursión -> Dibuja el subárbol izquierdo

    if node.get_right() is not None:
        plt.plot([x, x + espaciado], [y, y - 1], color='black')
        dibujar_bst(node.get_right(), x + espaciado, y - 1, espaciado / 2)

    plt.scatter(x, y, s=500, c='skyblue', edgecolors='black', zorder=3) # Dibuja el nodo. (x,y) son las coordenadas del nodo, s es el tamaño, zorder indica la capa
    plt.text(x, y, str(node.key), fontsize=8, color = 'grey') # Palabra
    plt.axis("off")

def plot_rbt(tree, letter):
    """
    Genera una visualización gráfica de un Árbol Rojo-Negro.

    Parámetros:
    - tree: Árbol binario a graficar
    - letter: String con la letra analizada (para el título del gráfico).

    Retorna:
    - None: Muestra el gráfico.
    """
    if tree.root == tree.NIL: return
    plt.figure(figsize=(10, 6))
    plt.title(f"RBT - Letra {letter.upper()}")

    dibujar_rbt(tree, tree.root, 0, 0, 4)
    plt.show()

def dibujar_rbt(tree, node, x, y, espaciado):
        """
        Posiciona y pinta los nodos del árbol rojo-negro

        Parámetros:
        - tree: Árbol Rojo-Negro
        - node: Nodo actual a dibujar.
        - x, y: Coordenadas en el plano
        - espaciado: Distancia horizontal para separar los hijos
        """
        if node == tree.NIL: 
            return

        if node.get_left() != tree.NIL:
            plt.plot([x, x - espaciado], [y, y - 1], color='black')
            dibujar_rbt(tree, node.get_left(), x - espaciado, y - 1, espaciado / 2)

        if node.get_right() != tree.NIL:
            plt.plot([x, x + espaciado], [y, y - 1], color='black')
            dibujar_rbt(tree, node.get_right(), x + espaciado, y - 1, espaciado / 2)
        
        if node.is_red():
            color = 'red'
        else:
            color = 'black'

        plt.scatter(x, y, s=500, color=color, edgecolors='black', zorder=3)
        plt.text(x, y, str(node.key), fontsize=8, color = 'gray')
        plt.axis("off")


# NOTA: En este apartado del proyeto se ha utilizado la Inteligencia Artifical para comprender la 
#   librería matplotlib, en específico las funciones de plot y scatter y la forma de graficar los
#   árboles para que queden los nodos espaciados, de diferentes colores y por niveles.