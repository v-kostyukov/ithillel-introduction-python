def reverse_it(n, i):
    return i if (n == 0) else reverse_it(n // 10, i * 10 + n % 10)


n = int(input('Введите число n: '))
print(reverse_it(n, 0))


# def reverse_it(n):
#     if n < 10:
#         print(n, end='')
#     else:
#         print(n % 10, end='')
#         return reverse_it(n // 10)
#
#
# # n = int(123456789)
# n = int(input('Введите число n: '))
# print('Число n : ', n)
# print('Число наоборот : ', end='')
# reverse_it(n)
