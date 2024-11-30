def password(number):
    pass_ = ""
    for i in range(1, number + 1):
        for j in range(i + 1, number + 1):
            if number % (i + j) == 0:
                pass_ += str(i) + str(j)
    return pass_

print('Введите число от 3 до 20: ')
num = int(input())
if 3 <= num <= 20:
    print(password(num))
