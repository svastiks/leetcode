class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        store = {}
        answer = []

        for n in nums:

            if n not in store:
                store[n] = 1
            else:
                store[n] += 1

        sort = sorted(store.items(), key=lambda item: item[1], reverse=True)

        return [item[0] for item in sort[:k]]
