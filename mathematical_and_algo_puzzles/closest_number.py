#code

def closest_number(n, m):
    # quotient
    q = int(n / m)
    n1 = q * m

    if (n * m) > 0:
        n2 = m * (q + 1)
    else:
        n2 = m * (q - 1)
    if abs(n-n1) < abs(n-n2):
        return n1
    else:
        return n2

if __name__ == '__main__':
    inputs = []
    num_test_cases = input()
    for i in range(0,int(num_test_cases)):
        number = input()
        inputs.append(number)
    for i in inputs:
        inputs = i.split(' ')
        print(closest_number(int(inputs[0]), int(inputs[1])))
