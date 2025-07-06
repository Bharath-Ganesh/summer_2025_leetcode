class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(idx, curr : TrieNode):
            for i in range(idx, len(word)):
                ch = word[i]
                if ch == '.':
                    for node in curr.children.values():
                        if dfs(i + 1, node):
                            return True
                    return False
                else:
                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]
            return curr.endOfWord
        return dfs(0, self.root)

if __name__ == '__main__':
    # word_dictionary = WordDictionary()
    # word_dictionary.addWord("bad")
    # word_dictionary.addWord("dad")
    # word_dictionary.addWord("mad")
    #
    # print(word_dictionary.search("pad"))  # False
    # print(word_dictionary.search("bad"))  # True
    # print(word_dictionary.search(".ad"))  # True
    # print(word_dictionary.search("b.."))  # True

    word_dictionary = WordDictionary()
    word_dictionary.addWord("a")
    word_dictionary.addWord("a")


    # print(word_dictionary.search("."))  # True
    # print(word_dictionary.search("a"))  # True
    # print(word_dictionary.search("aa"))  # False
    # print(word_dictionary.search("a"))  # True
    print(word_dictionary.search(".a"))  # False
    # print(word_dictionary.search("a."))  # False