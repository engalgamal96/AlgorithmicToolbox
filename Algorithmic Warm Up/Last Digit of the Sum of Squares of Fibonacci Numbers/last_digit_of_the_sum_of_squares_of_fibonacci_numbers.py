def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
#1800 is the sum for the period is && result is the sum
    result= int(n/60)*1800
    n=n%60
# f is list for fibonacci numbers
    f=[]
    f.append(0)
    f.append(1)
    if n<=1:
        return n
    else:
        for i in range(2,n+1,1):
            v=((f[i-1]+f[i-2])%10)**2
            f.append(v)
            result=result+v
    return result
if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
