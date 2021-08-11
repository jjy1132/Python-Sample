def mul(*values):
    output = 1
    for value in values:
        output *= value
    return output

print(mul(5,7,9,10))

print()

def f(x):
    return 2*x+1 #2x+1
#x**2+x*2+1 --> x+1의 제곱
print(f(10))
