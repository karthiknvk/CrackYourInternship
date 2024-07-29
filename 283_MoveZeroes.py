class Solution(object):
    def moveZeroes(self, nums):
      low=0
      high=len(nums)
      if high>1:
        while low<high:
          if nums[low]==0:
            while nums[low]==0 and low<high:
              nums.pop(low)
              nums.append(0)
              high=high-1
          low=low+1
      return nums