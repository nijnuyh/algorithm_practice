# programmers, phase1 : 약수의 합, python3
def solution(n):
    return sum([i for i in range(1,n+1) if n%i==0])
