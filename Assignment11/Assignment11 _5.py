def countzeroes(n):
    if n == 0:
        return 0
    return (1 if n%10 == 0 else 0) + countzeroes(n//10)
    
    

print(countzeroes(10102030405050607080))



