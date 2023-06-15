if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr1 = []
    for i in arr:
        if i not in arr1:
            arr1.append(i)
    arr1.remove(max(arr1))
    
    print(max(arr1))