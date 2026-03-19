def luckBalance(k, contests):
    important_luck = []
    total_luck = 0

    for luck, importance in contests:
        if importance == 0:
            total_luck += luck
        else:
            important_luck.append(luck)

    important_luck.sort(reverse=True)

    total_luck += sum(important_luck[:k])
    total_luck -= sum(important_luck[k:])

    return total_luck