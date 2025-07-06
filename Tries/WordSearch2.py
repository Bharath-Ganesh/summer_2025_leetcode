from typing import List


class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()
        for word in words:
            trie.insert(word)
        root = trie.root

        rows, cols = len(board), len(board[0])
        visited = set()
        res = []

        def dfs(row, col, path, node):
            key = (row, col)
            if row < 0 or col < 0 or row >= rows or col >= cols or key in visited:
                return

            if board[row][col] not in node.children:
                return


            visited.add(key)
            path.append(board[row][col])
            node = node.children[board[row][col]]
            if node.endOfWord:
                res.append("".join(path.copy()))
            dfs(row + 1, col, path, node)
            dfs(row, col + 1, path, node)
            dfs(row - 1, col, path, node)
            dfs(row, col - 1, path, node)
            path.pop()
            visited.remove(key)

        for r in range(rows):
            for c in range(cols):
                rootNode = root
                if board[r][c] in rootNode.children:
                    dfs(r, c, [], rootNode)

        return res

if __name__ == '__main__':
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath","pea", "eat", "rain"]
    sol = Solution()
    ans = sol.findWords(board, words)
    print(ans)