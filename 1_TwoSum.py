class Solution:
    def twoSum(self,nums,target):
      for i in range(len(nums)):
        for j in range(i+1,len(nums)):
          if nums[i]+nums[j]==target:
            list1=[i,j]
            return list1