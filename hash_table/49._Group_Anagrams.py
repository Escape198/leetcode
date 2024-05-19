class Solution:

    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())



anagram_dict = defaultdict()

for idx, ele in enumerate(strs):
    sortEle = ''.join(sorted(ele))
    anagram_dict[sortEle] = anagram_dict.get(sortEle, [])
    (anagram_dict[sortEle]).append(ele)

return anagram_dict.values()
