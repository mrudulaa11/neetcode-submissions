class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}

        for i in strs:
            count = [0] * 26
            for ch in i:
                index= ord(ch) - ord('a')
                count[index] += 1
            key = tuple(count)
            if key not in group:
                group[key] = []
            group[key].append(i)
        return list(group.values())