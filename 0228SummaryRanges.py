class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i, j = 0, 1
        output = []
        n = len(nums)

        if n == 0 : 
            return []

        start = nums[0]
        if n == 1 : 
            return [f"{start}"]

        while j < n :
            if nums[j] - 1 == nums[i]:
                j += 1
                i += 1
                continue
            if nums[j] - 1 != nums[i]:
                end = nums[i]
                if start == end : 
                    element = f"{start}"
                else:
                    element = f"{start}->{end}"
                output.append(element)
                start = nums[j]
                j += 1
                i += 1
        end = nums[i]
        if start == end : 
            element = f"{start}"
        else:
            element = f"{start}->{end}"
        output.append(element)

        return output
