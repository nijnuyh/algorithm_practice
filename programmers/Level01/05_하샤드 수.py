# programmers, phase1 : 하샤드 수, python3
def solution(x):
    return x % sum(int(i) for i in str(x))==0
