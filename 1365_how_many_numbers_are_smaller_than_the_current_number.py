class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        """
        Optimal Solution
        Time Complexity: O(nlogn), due to sorting
        Space Complexity: O(n)
        """

        newlist = sorted(nums)

        dicti = {}

        final = []

        for i, v in enumerate(newlist):
            if v not in dicti:
                dicti[v] = i

        for i in nums:

            final.append(dicti[i])

        return final

        """
        Brute force solution below

        Time Complexity: O(n^2)

        Space Complexity: O(n)
        
        listcount = []

        for i in nums:

            counter = 0

            for j in nums:

                if i != j and j < i:
                    counter+=1

            listcount.append(counter)

        return listcount
        """
        