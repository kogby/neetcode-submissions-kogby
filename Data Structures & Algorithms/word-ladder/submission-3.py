class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        candidates = [beginWord]
        count = 1
        if endWord not in wordList:
            return 0
        while len(candidates)!=0:
            count += 1
            next_words = []
            for now in candidates:
                for c in "abcdefghijklmnopqrstuvwxyz":
                    # print("now at",c)
                    for i in range(len(now)):
                        cand = now[:i] + c + now[i+1:]
                        if cand == endWord:
                            return count
                        if cand in wordList and cand != now:
                            next_words.append(cand)
                            wordList.remove(cand)
            candidates = next_words
        return 0
                        
