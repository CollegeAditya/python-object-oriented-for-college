def area(leng, bre = None):
    if bre == None:
        return leng*leng
    
    return leng*bre

print(area(4, 2))