class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #using dictionary would be easier 
        n = len(nums)
        dicter = {}
        for i in nums:
            if i not in dicter:
                dicter[i] = 1
            else:
                dicter[i] += 1
        n = n // 2
        for key, value in dicter.items():
            if value > n:
                return key

        return 0
