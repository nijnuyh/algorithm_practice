# programmers, phase1 : 자연수 뒤집어 배열로 만들기, python3
def solution(n):
    return [int(i) for i in str(n)][::-1]    # 배열할 때, 'reversed()' 말고 간단하게 뒤에 '[::-1]'로도 가능 
