class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        score = defaultdict(int)
        for w in words:
            test_str = ""
            for c in w:
                test_str += c
                score[test_str] += 1

        ans = []
        for w in words:
            test_str = ""
            this_score = 0
            for c in w:
                test_str += c
                this_score += score[test_str]
            ans.append(this_score)
        
        return ans