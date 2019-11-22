# 0 1 1 2 3 5 8 13 21 34


def fib(n):
    a, b = 0, 1
    result = [a]
    for i in range(n-1):
        a, b = b, a + b
        if a > n:
            break
        result.append(a)

    return result


# print(fib(30))


def simple_num(n):
    l = range(n)
    result, result_2 = [], []
    for i in l:
        a = l[i]
        for j in l:
            b = l[j]
            if a != 0 and b != 0 and a % b == 0:
                print(f'{a} % {b} = {a%b}')
                result.append(a)
    print(result)
    for i in result:
        if result.count(i) == 2:
            result_2.append(i)

    return list(set(result_2))


print(simple_num(10))


def fiv_and_simple(n):
    result = []
    for i in fib(n):
        for j in simple_num(n):
            if i == j:
                result.append(i)
    return result


# print(fiv_and_simple(30))
