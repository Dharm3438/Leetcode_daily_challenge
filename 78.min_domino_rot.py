'''
1007. Minimum Domino Rotations For Equal Row

In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
'''

class Solution {
    public int minDominoRotations(int[] A, int[] B) {
        int ans = min(
                f(A[0], A, B),
                f(B[0], A, B),
                f(A[0], B, A),
                f(B[0], B, A));
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
    
    private int min(int a, int b, int c, int d) {
        return Math.min(Math.min(Math.min(a, b), c), d);
    }

    /* Count number of rotations to make values in A equal to target. */
    private int f(int target, int[] A, int[] B) {
        int swap = 0;
        for (int i = 0; i < A.length; i++) {
            if (A[i] != target) {
                if (B[i] != target) {
                    return Integer.MAX_VALUE;
                } else {
                    swap++;
                }
            }
        }
        return swap;
    }
}