def sol():
    numbers = [int(x) for x in input().strip().split()]
    n = numbers[0]
    k = numbers[1]
    scores = [int(x) for x in input().strip().split()]
    scores.sort(reverse=True)
    score = scores[k]
    final_scores = []
    if score == 0:
        return 0
    for scores_ in scores:
        if scores_ >= score:
            final_scores.append(scores_)
    return(len(final_scores))
print(sol())
