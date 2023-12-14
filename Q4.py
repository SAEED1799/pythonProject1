# Trees and Graphs:
# Write a program to find the lowest common ancestor of two nodes in a binary
# Tree.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    if not root:
        return None

    if root.value == p or root.value == q:
        return root

    left_ancestor = lowest_common_ancestor(root.left, p, q)
    right_ancestor = lowest_common_ancestor(root.right, p, q)

    if left_ancestor and right_ancestor:
        return root

    return left_ancestor if left_ancestor else right_ancestor


# Write a program to find the shortest path between two nodes in a graph.

from collections import defaultdict, deque


def shortest_path(graph, start, end):
    if start == end:
        return [start]

    visited = set()
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        path = path + [current]

        if current == end:
            return path

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path))

    return None  # If there is no path


# Implement a binary search tree and write functions to insert, delete and search
# for elements.

class TreeNodeBST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def _min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return TreeNodeBST(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)

        return node

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if not node or node.value == value:
            return node

        if value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if not node:
            return None

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Node to be deleted found
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Node with two children: Get the inorder successor (smallest
            # in the right subtree)
            temp = _min_value_node(node.right)

            # Copy the inorder successor's content to this node
            node.value = temp.value

            # Delete the inorder successor
            node.right = self._delete(node.right, temp.value)

        return node
