class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict1, dict2 = {}, {}

        for word in s:
            if word not in dict1:
                dict1[word] = 1
            else:
                dict1[word] += 1
        
        for word in t:
            if word not in dict2:
                dict2[word] = 1
            else:
                dict2[word] += 1 
        
        return dict1 == dict2
