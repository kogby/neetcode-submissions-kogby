from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # use slide window to check if s2 has s1
        window_size = len(s1)
        if window_size > len(s2):
            return False

        s1_count = defaultdict(int)
        for c in s1:
            s1_count[c] += 1
        for i in range(len(s2) - len(s1)+1):
            window_word = s2[i:i+window_size]
            window_count = defaultdict(int)
            for c in window_word:
                window_count[c] += 1

            found = True
            print(s1_count, window_count)
            for c in s1:
                if s1_count[c] != window_count[c]:
                    found = False
                    break
            if found:
                return True
        return False
                
            