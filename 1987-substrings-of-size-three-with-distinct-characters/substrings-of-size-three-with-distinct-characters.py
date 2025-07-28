class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        k = 3
        for i in range(len(s) - k + 1):
            window = s[i:i + k]
            if len(set(window)) == k:
                count += 1
        return count
