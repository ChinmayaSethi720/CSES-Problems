# Question
# A permutation of integers 1,2,…,n is called beautiful if there are no adjacent elements whose difference is 1.
# Given n, construct a beautiful permutation if such a permutation exists.

# Link
# https://cses.fi/problemset/task/1070/

n= int(input())

if (n==2 or n==3):
    print("NO SOLUTION")
elif (n==4):
    print("3 1 4 2")
else:
    perm=[str(i) for i in range (1,n+1,2)]
    perm+=[str(i) for i in range (2,n+1,2)]
    print(" ".join(perm))

# author: Ashis-007
# profile: https://cses.fi/user/32353
# Solution: https://cses.fi/problemset/result/1135658/