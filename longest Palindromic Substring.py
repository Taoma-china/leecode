'''
最长回文子串：
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。


示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

方法：中心法
例如： a    b   a   b   a   b   a
       0    1   2   3   4   5   6
       
      分情况讨论，a可以是中心，a和b也可能是中心。 
      情况1：单个字母为中心
        设置 left=i-1 right=i+1 i从零开循环。
        i=0时，left=-1，right=1，比较left是否跟right相等，如若相等，left--，right++，往外拓展，直到不相等，保存left跟符合要求的substring长度（right-left-1）
        然后循环i。因为要求最长的substring。
      情况2：两个字母为中心
        i=0时，意味着left=0，right=1，先判断中心是否相等，然后left--，right++，往外拓展，直到不相等，保存符合要求left跟substring长度。

      我分别把left存到一个list里，把长度存到一个list里。然后用max求出最大长度，找到索引，就是包含left列表里索引位置。因为是一一对应的。然后输入s【left，长度】。

    
'''     


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
                
        
                a.append(left+1)
                b.append(right-left-1)
        if len(a)==0:
            return s[0]
        return s[a[b.index(max(b))]:max(b)+a[b.index(max(b))]]
    
    
    
