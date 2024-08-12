class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        apmore = []
        elemental = {}
        for i in nums:
            if i not in elemental:
                elemental[i] = 1
            else:
                elemental[i] += 1
        for key, value in elemental.items():
            if value > (n//3):
                apmore.append(key)
        
        return apmore
