# programmers, phase1 : 가운데 글자 가져오기, python3
def solution(s):
    center = int(len(s)/2)
    if len(s) % 2 != 0:
        return s[center]
    else:
        return s[center-1:center+1]
