class Solution(object):
    def reverseWords(self, s):
        list1=s.split()
        low=0
        high=len(list1)-1
        while low<high:
            temp=list1[high]
            list1[high]=list1[low]
            list1[low]=temp
            low=low+1
            high=high-1
        s=' '.join(list1)
        return s