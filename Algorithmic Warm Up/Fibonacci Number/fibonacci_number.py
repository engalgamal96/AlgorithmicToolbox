# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 500
    f=[]
    f.append(0)
    f.append(1)
    if n<=1:
        return n
    else:
        for i in range(2,n+1,1):
            f.append(f[i-1]+f[i-2])
        return f[n]

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
