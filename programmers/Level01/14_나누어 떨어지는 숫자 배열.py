# programmers, phase1 : 나누어 떨어지는 숫자 배열, python3
def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor==0]) or [-1]
