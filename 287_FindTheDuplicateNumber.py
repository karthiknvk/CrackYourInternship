class Solution(object):
    def findDuplicate(self, nums):
      dict1={}
      for item in nums:
         if item not in dict1:
            dict1[item]=1
         else :
            return item