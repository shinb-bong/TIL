# 비트연산

import sys
from itertools import combinations

input = sys.stdin.readline

def word2bit(word):
    bit = 0
    for char in word:
        bit = bit | (1 << ord(char) - ord('a')) # ord 아스키

        # 예를 들어 a 라면 1 
        # b라면 10 이걸 합집합하면
        # 11
    return bit

N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]
bits = list(map(word2bit, words))
base = word2bit('antic')

if K < 5:
    print(0)

else:
    alphabet = [1 << i for i in range(26) if not (base & 1 << i)] # 만약 이미 만든것이 아니라면 

    answer = 0 
    for combinations in combinations(alphabet,K-5):
        know_bit = sum(combinations) | base
        count = 0
        for bit in bits:
            if bit & know_bit == bit: # know_bit 전부를 알면 1로 and 를 했을 때 똑같은 경우가 나온다.
                count += 1
            answer = max(answer,count)

    print(answer)

