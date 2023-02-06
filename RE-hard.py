#https://leetcode.com/problems/regular-expression-matching/description/
#regular expression matching
#With python3, using package re
import re

#full match will have a time execeed for last case.
def isMatch(self, s: str, p: str) -> bool:
        res = re.match(p,s)
        if not res:
            return False
        else:
            return len(s)==res.end()

def isMatch2(self, s: str, p: str) -> bool:
    return re.fullmatch(p,s)

#dynamic programming
def isMatch3(self, s: str, p: str) -> bool:
    n_s=len(s)
    n_p=len(p)
    dp=[[False]*(n_p+1) for _ in range(n_s+1)]
    dp[0][0]=True
        
    #For empty string but the "*" in pattern might return True
    for i in range(1,n_p+1):
        if p[i-1]=="*":
            dp[0][i]=dp[0][i-2]
        
    for i in range(1,n_s+1):
        for j in range(1,n_p+1):
            #When the character in string matches with the patter or the pattern has '.', which accepts any character
            if s[i-1]==p[j-1] or p[j-1]=='.':
                dp[i][j]=dp[i-1][j-1]
            #When the pattern has "*", this shows that we need to check the [j-2] for the character, which can be the string character or '.'. In this case we will check the [i-1][j], to check if the character except the current one is True.
                
            elif p[j-1]=="*":
                dp[i][j]=dp[i][j-2]
                if p[j-2]=='.' or p[j-2]==s[i-1]:
                    dp[i][j]=dp[i][j] or dp[i-1][j]

    return dp[n_s][n_p]