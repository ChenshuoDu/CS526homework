from dataclasses import dataclass
from typing import Optional, List
import random

@dataclass
class Node:
    value: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None

class BST:
    def __init__(self):
        self.root: Optional[Node] = None

    def add(self, value: int) -> None:
        self.root = self._add(self.root, value)

    def delete(self, value: int) -> None:
        self.root = self._delete(self.root, value)

    def find(self, value: int) -> bool:
        return self._find(self.root, value)

    def print_tree(self) -> None:
        lines: List[str] = []
        self._collect_lines(self.root, 0, lines)
        print("\n".join(lines) if lines else "(empty)")

    def _add(self, node: Optional[Node], value: int) -> Node:
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._add(node.left, value)
        elif value > node.value:
            node.right = self._add(node.right, value)
        return node

    def _delete(self, node: Optional[Node], value: int) -> Optional[Node]:
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            succ_parent = node
            succ = node.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            node.value = succ.value
            if succ_parent.left is succ:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right
        return node

    def _find(self, node: Optional[Node], value: int) -> bool:
        while node:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False

    def _collect_lines(self, node: Optional[Node], depth: int, out: List[str]) -> None:
        if not node:
            return
        self._collect_lines(node.right, depth + 1, out)
        out.append("    " * depth + f"{node.value}")
        self._collect_lines(node.left, depth + 1, out)

def demo_bst(random_seed: Optional[int] = None) -> None:
    if random_seed is not None:
        random.seed(random_seed)
    bst = BST()
    n = random.randint(5, 50)
    values = random.sample(range(1, 1001), n)
    print("Random Input Set:", values)
    for v in values:
        bst.add(v)
    print("\nInitial Tree:")
    bst.print_tree()

    to_add = []
    while len(to_add) < 3:
        cand = random.randint(1, 1000)
        if not bst.find(cand):
            to_add.append(cand)
    for v in to_add:
        print(f"\nAdd {v}:")
        bst.add(v)
        bst.print_tree()

    to_delete = random.sample(values + to_add, 3)
    for v in to_delete:
        print(f"\nDelete {v}:")
        bst.delete(v)
        bst.print_tree()

    pos = random.choice(values + to_add)
    neg = None
    while True:
        cand = random.randint(1, 1000)
        if not bst.find(cand):
            neg = cand
            break
    print(f"\nFindNode({pos}) ->", "Found" if bst.find(pos) else "Not Found")
    print(f"FindNode({neg}) ->", "Found" if bst.find(neg) else "Not Found")

if __name__ == "__main__":
    demo_bst()
