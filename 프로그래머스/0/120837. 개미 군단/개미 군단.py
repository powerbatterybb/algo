def solution(hp):
    answer = 0
    
    a=0
    b=0
    c=0
    
    a = hp//5
    hp = hp%5
    
    b = hp//3
    hp = hp%3
    
    c = hp
    
    answer = a+b+c
    
    return answer