class TrieNode:
    def __init__(self, val: str, children: dict, is_end_of_word: bool = False):
        self.val = val
        self.children = children
        self.is_end_of_word = is_end_of_word

    def fromWord(self, word: str) -> 'TrieNode':
        if not word:
            return None

        if len(word) == 1:
            return TrieNode(word[0], {}, is_end_of_word=True)
        else: 
            children = {}
            children[word[1]] = self.fromWord(word[1:])
            return TrieNode(word[0], children)

class PrefixTree:

    def __init__(self):
        self.root = TrieNode('', {})

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode(letter, {})
            node = node.children[letter]
        node.is_end_of_word = True


    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True
        
        