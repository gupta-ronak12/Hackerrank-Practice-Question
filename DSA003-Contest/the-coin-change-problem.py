def getWays(n, c):
    ways = [0]*(n+1)
    
    ways[0] = 1  
    for value in c:
            for amount in range(value, n+1):
                ways[amount] += ways[amount - value]
    return ways[n]
