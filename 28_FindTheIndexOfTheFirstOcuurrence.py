class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(0,(len(haystack)-len(needle))+1):
            if haystack[i]==needle[0]:
                print("enterinn in",haystack[i])
                flag=True
                for j in range(1,len(needle)):
                    print(haystack[i+j],'->>',needle[j])
                    if haystack[i+j]!=needle[j]:
                        flag=False  
                        continue                     
                if flag==True:
                    return i
        return -1