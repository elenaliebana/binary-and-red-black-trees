# Binary Search Trees vs. Red-Black Trees

Python implementation of a **binary search tree** (BST) and a **red-black tree**, used to index a Spanish word list by initial letter and compare how both structures behave. Course project for Algorithms and Data Structures.

## What is inside

| File | Content |
|---|---|
| `BinaryTree.py` | `Node` and `BinaryTree`: insertion, deletion, height, number of nodes and leaves, skew check, longest path, in-order / pre-order / post-order / level-order traversals, paths to a leaf of a given length |
| `RedBlackTree.py` | `RBNode` and `RedBlackTree` with the same operations plus left/right rotations and the insertion and deletion fix-ups that keep the tree balanced |
| `Opcional.py` | matplotlib drawings of both trees |
| `Proyecto.py` | Main program |
| `palabras_RAE_cleaned_noaccents.txt` | Word list (one word per line, no accents) |

## How it works

`Proyecto.py` asks for up to three letters and for the insertion order:

- `D` – words are inserted in file order (alphabetical): the BST degenerates into a long chain;
- `A` – words are inserted in random order.

For every letter it builds both trees and prints the root and its children, height, number of nodes and leaves, whether the tree is skewed, the longest path and the paths to a leaf of length 4. It then compares the heights: the red-black tree rotates nodes to stay balanced, so it is much shallower than the BST when words arrive in alphabetical order. It can also draw both trees (slow for letters with many words; `k`, `x` and `w` are good to try).

## Run it

Requires Python 3 and `matplotlib` (only for the drawings).

```bash
pip install matplotlib
python Proyecto.py
```
