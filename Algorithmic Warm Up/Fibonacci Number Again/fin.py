def fibonacci_number_again(n,m):
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
    n,m=map(int, input().split())
    print(fibonacci_number_again(n,m))
