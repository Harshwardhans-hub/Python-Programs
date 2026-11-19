"""Trie (prefix tree) for efficient word and prefix lookup."""

from __future__ import annotations


class _TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, _TrieNode] = {}
        self.is_word = False


class Trie:
    """Case-sensitive trie that stores strings without normalizing them."""

    def __init__(self) -> None:
        self._root = _TrieNode()
        self._size = 0

    def insert(self, word: str) -> None:
        if not isinstance(word, str):
            raise TypeError("word must be a string")
        node = self._root
        for character in word:
            node = node.children.setdefault(character, _TrieNode())
        if not node.is_word:
            node.is_word = True
            self._size += 1

    def _find_node(self, prefix: str) -> _TrieNode | None:
        node = self._root
        for character in prefix:
            node = node.children.get(character)
            if node is None:
                return None
        return node

    def search(self, word: str) -> bool:
        if not isinstance(word, str):
            raise TypeError("word must be a string")
        node = self._find_node(word)
        return bool(node and node.is_word)

    def starts_with(self, prefix: str) -> bool:
        if not isinstance(prefix, str):
            raise TypeError("prefix must be a string")
        return self._find_node(prefix) is not None

    def words_with_prefix(self, prefix: str = "") -> list[str]:
        if not isinstance(prefix, str):
            raise TypeError("prefix must be a string")
        node = self._find_node(prefix)
        if node is None:
            return []
        result: list[str] = []

        def collect(current: _TrieNode, word: str) -> None:
            if current.is_word:
                result.append(word)
            for character in sorted(current.children):
                collect(current.children[character], word + character)

        collect(node, prefix)
        return result

    def __len__(self) -> int:
        return self._size
