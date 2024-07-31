class Solution(object):
    def countBits(self, n):
      list1=[]
      for i in range(n+1):
           list1.append(bin(i)[2:].count('1'))
      return list1