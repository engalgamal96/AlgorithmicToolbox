def money_change(money):
    assert 0 <= money <= 10 ** 3
    n_10 = int(money / 10)
    n_5 = int((money % 10) / 5)
    n_1 = int(((money % 10) % 5) / 1)
    return n_10 + n_5 + n_1

if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
