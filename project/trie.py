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

    def __repr__(self):
        return f"NODE({self.children})"


class Trie:

    def __init__(self):
        """
        Initializes new instance of Trie class with a root node
        """
        self.root = TrieNode()

    def insert(self, phone_number: str, cost: float):
        """
        Inserts new item into trie
        """
        node = self.root
        # iterate over to keep appending numbers to tree
        for num in phone_number:
            num = int(num)
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
        if phone_number[0] == "+":  # Clean input
            phone_number = phone_number[1:]

        node = self.root
        cost = 0
        # traverse down tree by each digit in phone number
        for num in phone_number:
            num = int(num)
            if node.children[num] is not None:
                node = node.children[num]
                if node.cost is not None:
                    cost = node.cost
        # return the cost at node if there is one
        # if not return the stored cost from higher up in tree
        return node.cost if node.cost is not None else cost
