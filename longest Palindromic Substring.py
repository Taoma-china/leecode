class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return s
        if len(s)==1:
            return s
        


        a=[]
        b=[]
        allofpalindrome = {"0":"0"}
        length_s= len(s)
        for i in range(length_s):
            left=i-1
            right=i+1
            if left >=0 and right<length_s and s[left]==s[right]:
                while(s[left]==s[right]):
                    
                    left=left-1
                    right=right+1
                    

                    if left<0 or right>=length_s:
                        break
                allofpalindrome[left+1]=(right-left-1)
                a.append(left+1)
                b.append(right-left-1)
            left=i
            right=i+1
            if left>=0 and right<length_s and s[left]==s[right]:

                while(s[left]==s[right]):
                    left=left-1
                    right=right+1

                    if left<0 or right>=length_s:
                        break
                allofpalindrome[left+1]=(right-left-1)
        
                a.append(left+1)
                b.append(right-left-1)
        if len(a)==0:
            return s[0]
        return s[a[b.index(max(b))]:max(b)+a[b.index(max(b))]]