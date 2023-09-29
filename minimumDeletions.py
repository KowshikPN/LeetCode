def longestcommonsubsequence(s1,s2,m,n):
    if m == 0 or n == 0:
        return 0

    if s1[m-1] == s2[n-1]:
        return 1 + longestcommonsubsequence(s1,s2,m-1,n-1)
    else:
        return max(longestcommonsubsequence(s1,s2,m,n-1),longestcommonsubsequence(s1,s2,m-1,n))



s1 = "pot"
s2 = "clot"

lcs = longestcommonsubsequence(s1,s2,len(s1),len(s2))
print(len(s1)+len(s2) - 2*lcs)

'''
Time Complexity: lcs --> O(2^n)

'''