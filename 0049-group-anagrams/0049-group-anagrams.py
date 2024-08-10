class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            li[sorted_word].append(word) 
        return li.values()