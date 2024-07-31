class Solution(object):
    def majorityElement(self, nums):
        dict1={}
        for item in nums:
            if item not in dict1:
                dict1[item]=1
            else:
                dict1[item]=dict1[item]+1
        for key,value in dict1.items():
            if value>len(nums)/2:
                return key
