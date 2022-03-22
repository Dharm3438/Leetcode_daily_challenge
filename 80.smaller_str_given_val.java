// 1663. Smallest String With A Given Numeric Value

// https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

class Solution {
    public String getSmallestString(int n, int k) {
        char[] answer = new char[n];
        Arrays.fill(answer, 'a');
        k = k - n;
        while (n > 0 && k > 0) {
            int min = Math.min(25, k);
            answer[--n] = (char) (min + 'a');
            k -= min;
        }
        return String.valueOf(answer);
    }
}