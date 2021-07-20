def solution(participant, completion):
    p = {}
    for s in participant:
        if s in p:
            p[s] = p[s] + 1
            continue
        p[s] = 0

    for s in completion:
        p[s] = p[s] - 1

    for s in participant:
        if p[s] == 0:
            answer = s

    return answer
