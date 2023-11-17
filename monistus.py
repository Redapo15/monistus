xy = list(map(int, input().split()))
X = xy[1]
Y = xy[0]
num = 0

def parx(x):
    if x % 2 != 0:
        return x**2 - (Y-1)
    else:
        return (x-1)**2 + 1 + (Y-1)
def pary(y):
    if y % 2 == 0:
        return y**2 - (X-1)
    else:
        return (y-1)**2 + 1 + (X-1)
if Y < X:   
    num = parx(X)
elif Y > X:  
    num = pary(Y)
if X == Y:
    if Y % 2 == 0:
        num = Y**2 - (X-1)
    else:
        num = X**2 - (Y-1)
print(num)