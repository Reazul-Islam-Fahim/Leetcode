from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.name = ""
        self.is_deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()

        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode()
                    node.children[folder].name = folder
                node = node.children[folder]

        serial_map = defaultdict(list)

        def serialize(node):
            if not node.children:
                return ""
            items = []
            for child_name in sorted(node.children):
                child_serial = serialize(node.children[child_name])
                items.append(f"{child_name}({child_serial})")
            serial = "".join(items)
            serial_map[serial].append(node)
            return serial

        serialize(root)

        for nodes in serial_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.is_deleted = True

        res = []

        def dfs(node, path):
            for name, child in node.children.items():
                if not child.is_deleted:
                    res.append(path + [name])
                    dfs(child, path + [name])

        dfs(root, [])
        return res
