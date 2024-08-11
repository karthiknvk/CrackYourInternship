class Solution(object):
    def isValid(self, s):
        stack=[]
        characters={')':'(',']':'[','}':'{'}
        for i in range(len(s)):
            if s[i] in characters:
                if characters[s[i]] in stack and characters[s[i]]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if not stack:
            return True 
        else:
            return False 