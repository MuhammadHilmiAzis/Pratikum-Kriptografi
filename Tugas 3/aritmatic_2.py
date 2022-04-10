#to computer x^y mod m
def power(x,y,m):
    if (y == 0):
        return 1
    p = power(x, y // 2, m) % m
    p = (p * p) % m
    return p if(y % 2 == 0) else (x * p) % m
x = 27324678765465536
y = 65536
m =65537
print(power(x,y,m))