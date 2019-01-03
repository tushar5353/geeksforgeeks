
#code

def is_armstrong(number):
    n = sum([int(i)**3 for i in list(number)])
    return n==int(number)
    
if __name__ == '__main__':
    num_test_cases = input()
    for i in range(0,int(num_test_cases)):
        number = input()
        if is_armstrong(number):
            print("Yes")
        else:
            print("No")
