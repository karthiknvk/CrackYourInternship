class Solution(object):
    def findDuplicates(self, nums):
      nums.sort()
      low=0
      high=len(nums)-1
      flag=False
      while low<high:
        if  nums[low]==nums[low+1] and flag==True:
          nums.pop(low)
          high=high-1
          flag=False
        elif nums[low]!=nums[low+1]:
          nums.pop(low)
          high=high-1
          flag=False
        elif nums[low]==nums[low+1]:
          low=low+1
          flag=True
      nums.pop(low)      
      return nums