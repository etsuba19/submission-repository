class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        answer = []
        
        for index, number in enumerate(nums):
            complement = target - number
            if complement in nums[index + 1:]:
                return [index, nums[index+1: ].index(complement) + index + 1] 
                #we add the index because the sliced part doesnt include it
                #we add one becuase after the slicing the array would be 0 indexed
                #so we added both to get the correct index of the original list
