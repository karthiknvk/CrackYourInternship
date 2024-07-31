class Solution(object):
    def removeDuplicates(self, nums):
        print(nums)
        ele=nums[0]
        low=1
        high=len(nums)
        while low<high:
            if nums[low]==ele:
                nums.pop(low)
                high=high-1
            else:
                ele=nums[low]
                low=low+1
                continue
        return len(nums)