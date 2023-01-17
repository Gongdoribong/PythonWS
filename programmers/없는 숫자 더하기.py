def solution(numbers):
    return sum([x for x in range(10) if x not in numbers])

print(solution([5,8,4,0,6,7,9]))