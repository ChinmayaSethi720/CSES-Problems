# You are given an array of n integers, and your task is to find two values (at distinct positions) whose sum is x.
#https://cses.fi/problemset/task/1640

def sumOfTwo(array, targetSum):
    nums = {}
    for num in array:
        if targetSum - num in nums:
            return [(array.index(targetSum - num))+1, (array.index(num))+1]
        else:
            nums[num] = True

size, target_sum = input().split()
l = input()
array = list(map(int, l.split(' ')))

lst = sumOfTwo(array, int(target_sum))

if len(lst) == 0:
    print("IMPOSSIBLE")
else:
    for i in range(len(lst)):
        print(lst[i], end=" ")

# author : PrernaBabber
# https://cses.fi/user/32267