def Trapecium_mult(a,b,n):
    h = (b-a)/n
    print('h = {}'.format(h))

    sum = func_tointegrate(a)
    segment = a + h

    for i in range(n-1):
        sum = sum + 2*func_tointegrate(segment)
        segment = segment + h

    #print(segment)
    #print(sum)

    sum = sum + func_tointegrate(b)
    integral = h * sum/2

    return 'I = {}'.format(integral)

def func_tointegrate(x):
    result = 0.2 +25*x -200*x**2 + 675*x**3 -900*x**4 + 400*x**5
    return result


for n in range(2,11):
    print(Trapecium_mult(0,0.8,n))
    print('')
