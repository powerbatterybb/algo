def solution(my_string, alp):
    answer = ''
            
    a = alp.upper()
    
    
    #for i in range(len(my_string)):
        #if my_string[i] == alp:
            #my_string[i] = a
            
    answer = my_string.replace(alp, a)
    
    return answer