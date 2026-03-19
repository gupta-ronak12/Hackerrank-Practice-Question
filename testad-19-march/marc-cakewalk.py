def marcsCakewalk(calorie):
    calorie.sort(reverse = True)
    miles = 0
    for i in range(len(calorie)):
        miles += 2**i * calorie[i]
    return miles