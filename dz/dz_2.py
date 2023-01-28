a = int(input("Введите число от 1 до 99: "))
c = a
c = c % 10

if 11 <= a <= 14:
    print(a, "копеек")
elif a > 99:
    print("Ошибка")
else:
    if c == 1:
        print(a, "копейка")
    if 2 <= c <= 4:
        print(a, "копейки")
    if 5 <= c <= 9 or c == 0:
        print(a, "копеек")




