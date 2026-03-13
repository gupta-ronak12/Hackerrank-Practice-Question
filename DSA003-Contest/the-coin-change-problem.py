# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c

def getWays(n, c):
    ways = [0]*(n+1)
    
    ways[0] = 1  
    for value in c:
            for amount in range(value, n+1):
                ways[amount] += ways[amount - value]
    return ways[n]