if __name__ == '__main__':
    from collections import Counter
    python_students = []
    
    N = int(input())
    
    for _ in range(N):
        name = input()
        score = float(input())
        _ = [name, score]
        python_students.append(_)
    new_list= []
    for i in range(N):
        new_list.append(python_students[i][1])
    
    new_list.remove(min(new_list))
    Division = min(new_list)
    
    L =[]
    
    for i in range(N):
        
        if  python_students[i][1] == Division:
            L.append(python_students[i][0])
        else:
            0 == 0    
        
    for i in sorted(L):
        print(i)