import math
import sys

input = sys.stdin.readline

def find_one(n, k):
    if len(answer) == N - 1:
        answer.append(numbers[-1])
        return

    numberOfCases = math.factorial(n) // n
    sequence = math.ceil(k / numberOfCases)
    answer.append(numbers.pop(sequence))

    find_one(n-1, k-(numberOfCases*(sequence-1)))


def find_k():
    n = N
    for num in K:
        numberOfCases = math.factorial(n) // n
        idx = numbers.index(num)
        if len(numbers) == 2:
            idx += 1
            answer.append(numberOfCases*idx)
            return
        numbers.pop(idx)
        answer.append(numberOfCases*idx)
        n -= 1

N = int(input())
tmp_input = list(map(int, input().split()))
order = tmp_input.pop(0)
if order == 1:
    K = tmp_input[0]
    numbers = [x for x in range(N+1)]
    answer = []
    find_one(N,K)
    print(' '.join(list(map(str, answer))))

else:
    K = tmp_input
    numbers = [x for x in range(1, N+1)]
    answer = []
    find_k()
    print(sum(answer))