#code

def convert_to_decimal(number):
    decimal_value = 0
    temp = number
    base_value = 1

    while(temp):
        decimal_value += (temp % 10) * base_value
        base_value = base_value * 2
        temp = temp // 10

    return decimal_value

if __name__ == '__main__':
    inputs = []
    num_test_cases = input()
    for i in range(0,int(num_test_cases)):
        number = input()
        inputs.append(number)
    for i in inputs:
        x = convert_to_decimal(int(i))
        print(x)
