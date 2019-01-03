#code

def is_prime(number):
    if number in [2, 3]:
        return "Yes"
    for i in range(2, number):
        if number%i == 0:
            return "No"
    
    return "Yes"

if __name__ == '__main__':
    inputs = []
    num_test_cases = input()
    for i in range(0,int(num_test_cases)):
        number = input()
        inputs.append(int(number))

    for i in inputs:
        print(is_prime(i))
