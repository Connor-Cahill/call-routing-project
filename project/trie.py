#!python

class TrieNode:
    """
        TrieNode is the node for our Trie Class
    """
    def __init__(self):
        """
        Initializes new TrieNode
        """
        self.children = [None]*10
        self.cost = None

class Trie:

    def __init__(self):
        """
        Initializes new instance of Trie class with a root node
        """
        self.root = TrieNode()

    def insert(self, phone_number: str, cost: int):
        """
        Inserts new item into trie
        """
        node = self.root
        # iterate over to keep appending numbers to tree 
        for num in phone_number:
            if node.children[num] is None:
                node.children[num] = TrieNode()
            node = node.children[num]
        if node.cost is not None:
            if cost > node.cost:
                return
        node.cost = cost

    def search(self, phone_number: str) -> str:
        """
        Searches for a phone number in trie and returns cost
        """
        node = self.root




