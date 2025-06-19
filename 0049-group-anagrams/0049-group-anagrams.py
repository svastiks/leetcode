class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        storage = {}

        for string in strs:
            
            # sorts string into a list of characters
            sorted_characters = sorted(string)

            #joins the characters into a string
            sort = ''.join(sorted_characters)
            
            #creates entry if non existing
            storage[sort] = storage.get(sort, [])

            #if key in map then append the string
            if sort in storage:
                storage[sort].append(string)

        #return map values as a list so List[Lists]
        return list(storage.values())
            
        