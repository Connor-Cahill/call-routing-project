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
            num = int(num)  # cast to int b/c used as index
            # check if there is a child at index
            # if not then add Node
            if node.children[num] is None:
                node.children[num] = TrieNode()
            # traverse down tree
            node = node.children[num]

        # check to see if the current node has a cost property
        # if it does see if it is less than or greater than param cost value
        if node.cost is not None:
            if cost > node.cost:
                return
        # set nodes cost to the cost passed as param
        # only happens if there was no cost or the previous cost
        # was greater than
        node.cost = cost

    def search(self, phone_number: str) -> str:
        """
        Searches for a phone number in trie and returns cost
        """
        if phone_number[0] == "+":  # Clean input
            phone_number = phone_number[1:]

        # start traversing from root node
        node = self.root
        # cost var to keep track of
        # costs as we traverse down tree
        cost = 0
        # traverse down tree by each digit in phone number
        for num in phone_number:
            num = int(num)
            # if there is a child node in that index
            # traverse down
            if node.children[num] is not None:
                node = node.children[num]
                # check if node has a cost property
                # if True assign to our cost var
                if node.cost is not None:
                    cost = node.cost
        # return the cost at node if there is one
        # if not return the stored cost from higher up in tree
        return node.cost if node.cost is not None else cost
