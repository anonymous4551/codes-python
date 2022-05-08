def recurse(k):
    if(k > 0):
        result = k + recurse(k - 1)
        print(result)
    else:
        result = 0
    return result 
print("\n\n Recussion result it : ")   
recurse(10)
