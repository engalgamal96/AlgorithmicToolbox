# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    f=[]
    f.append(0)
    f.append(1)
    if n<=1:
        return n
    else:
        i=2
        while i!= 0:
            if f[i-1] ==0 and f[i-2]==1:
                break
            else:
                f.append((f[i-1]+f[i-2]) % m)
            i=i+1
    f.pop()
    x=len(f)
    y=(n % x)
    return (f[y])

if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))