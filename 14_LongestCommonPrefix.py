class Solution(object):
    def longestCommonPrefix(self, strs):
        prefixstring=[]
        flag=True
        for i in range(len(min(strs,key=len))):
            for j in range(1,len(strs)):
                if strs[j][i]!=strs[0][i]:
                    flag=False
                    break
            if flag==True:
                prefixstring.append(strs[0][i])
            else:
                break
        return ''.join(prefixstring)