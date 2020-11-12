def simpson_rule(a,b,n):
    """Calculates an integral using Simpson's 1/3 rule for multiple applications"""
    h = (b-a)/n
    print('h = {}'.format(h))

    sum = func_tointegrate(a)
    segment = a + h

    for i in range(1,n):

        if i % 2 == 0:
            sum = sum + 2*func_tointegrate(segment)
        else:
            sum = sum + 4*func_tointegrate(segment)

        segment = segment + h

    #print(segment)
    #print(sum)

    sum = sum + func_tointegrate(b)
    integral = h * sum/3

    return 'I = {}'.format(integral)

def func_tointegrate(x):
    result = 0.2 +25*x -200*x**2 + 675*x**3 -900*x**4 + 400*x**5
    return result

print(simpson_rule(0,0.8,4))
