#code

def is_palindrome(number):
    return number[::-1] == number

if __name__ == '__main__':
    num_test_cases = input()
    for i in range(0,int(num_test_cases)):
        number = input()
        num_string = str(sum([int(i) for i in list(number)]))
        if is_palindrome(num_string):
            print("YES")
        else:
            print("NO")
