#code

def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)

def nPr(n, r):
    n = int(n)
    r = int(r)
    nPr = factorial(n)//factorial(n - r)
    return nPr

if __name__ == '__main__':
    inputs = []
    num_test_cases = input()
    for i in range(0,int(num_test_cases)):
        number = input()
        inputs.append(number)
    for i in inputs:
        inputs = i.split(' ')
        x = nPr(inputs[0], inputs[1])
        print(x)
