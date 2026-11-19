class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #need to use map to store chars and how many times they appear
        map1 = {}
        map2 = {}

        for i in s:
            if i not in map1:
                map1[i] = 1
            else:
                map1[i] += 1

        for j in t:
            if j not in map2:
                map2[j] = 1
            else:
                map2[j] += 1
        
        if len(map1) != len(map2):
            return False

        for i in s:
            if i not in map2:
                return False
            if map1[i] != map2[i]:
                return False
        
        return True
        