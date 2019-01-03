#code
#nth_term = first_term * (ratio^n-1)

import math

def give_nth_value_of_gp_series(series, n):
    ratio = int(series[1])/int(series[0])
    return math.floor(int(series[0]) * (ratio ** (n-1)))

if __name__ == '__main__':
    series = []
    nth_term = []
    num_test_cases = input()
    for i in range(0,int(num_test_cases)):
        s = input()
        series.append(s)
        n = int(input())
        nth_term.append(n)

    count = 0
    for i in series:
        series = i.split(" ")
        print(give_nth_value_of_gp_series(series, nth_term[count]))
        count += 1
