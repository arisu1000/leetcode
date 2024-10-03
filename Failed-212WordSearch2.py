#https://leetcode.com/problems/word-search-ii/description

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #Step 1: Construct the Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        # Step 2: Backtracking function
        def backtrack(i, j, parent):
            char = board[i][j]
            node = parent.children[char]

            # Check if we find a word
            if node.word:
                result.add(node.word)
                node.word = None #Avoid duplicate entries

            # Mark the current cell as visited
            board[i][j] = '#'

            # Explore the neighbors in 4 directions: up, right, down, left
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] in node.children:
                    backtrack(x, y, node)

            # Restore the current cell
            board[i][j] = char

            # Optimization: Remove the leaf node
            if not node.children:
                parent.children.pop(char)

        # Step 3: Use backtracking to search for words in the board
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    backtrack(i, j, root)

        return list(result)
    

s = Solution()
print(s.findWords([["o","a","a","n"],
             ["e","t","a","e"],
             ["i","h","k","r"],
             ["i","f","l","v"]], 
            ["oath","pea","eat","rain"]), 
            ["eat","oath"])


print(s.findWords([["a","b"],
            ["c","d"]],
            ["abcb"]), 
            [])