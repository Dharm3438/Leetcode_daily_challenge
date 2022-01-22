'''
1510. Stone Game IV

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.

https://leetcode.com/problems/stone-game-iv/
'''

class Solution:
    def winnerSquareGame(self, n):
        @lru_cache(None)
        def dfs(state):
            if state == 0: return False
            for i in range(1, int(math.sqrt(state))+1):
                if not dfs(state - i*i): return True
            return False
        
        return dfs(n)