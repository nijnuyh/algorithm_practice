# programmers, phase1 : 문자열 다루기 기본, python3
def solution(s):
    if (len(s)==4 or len(s)==6) and s.isdigit():
        return True
    else:
        return False
    
