# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n, arr):

    candies = [1]*n
    
    for i in range(1,n):
        if arr[i] > arr[i -1]:
            candies[i] = candies[i - 1]+1
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i + 1] + 1
    return sum(candies)
