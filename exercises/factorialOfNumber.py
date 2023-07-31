def getfactorial(n):
    output = 1
    for n in range(1, n + 1):
        output = n * output
        print('out', output, 'num', n)

    return output


print(getfactorial(5))
