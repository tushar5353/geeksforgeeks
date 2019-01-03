#code

def gcd(a, b):
    a = int(a)
    b = int(b)

    if a == 0:
        return b
    if b == 0:
        return a

    if a == b:
        return a

    if a > b:
        return gcd(a-b, b)
    return gcd(a, b-a)

if __name__ == '__main__':
    inputs = []
    num_test_cases = input()
    for i in range(0,int(num_test_cases)):
        number = input()
        inputs.append(number)
    for i in inputs:
        inputs = i.split(' ')
        print(gcd(inputs[0], inputs[1]))
