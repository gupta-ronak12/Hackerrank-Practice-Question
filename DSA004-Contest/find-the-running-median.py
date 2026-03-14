def runningMedian(a):
    import heapq
    lhh = [] #lower half heap - lhh
    uhh = []  #upper half heap - uhh
    running_medians = []     
    for current_value in a:
        if not lhh or current_value <= -lhh [0]:
            heapq.heappush(lhh, -current_value)
        else:
            heapq.heappush(uhh, current_value)        
        if len(lhh) > len(uhh) + 1:
            heapq.heappush(uhh, -heapq.heappop(lhh))
        elif len(uhh) > len(lhh) + 1:
            heapq.heappush(lhh, -heapq.heappop(uhh))          
        if len(lhh) == len(uhh):
            median = (-lhh[0] + uhh[0])/2
        elif len(lhh) > len(uhh):
            median = float(-lhh[0])
        else:
            median = float(uhh[0])
        running_medians.append(median)
    return running_medians