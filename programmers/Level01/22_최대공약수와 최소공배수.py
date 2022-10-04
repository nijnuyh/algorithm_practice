# programmers, phase1 : 최대공약수와 최소공배수, python3
def solution(n, m):
    a, b = max(n,m), min(n,m)
    while b>0:
        a, b = b, a%b
        answer = [a, int((n*m)/a)]
    return answer
