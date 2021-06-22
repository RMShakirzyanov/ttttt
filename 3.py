s = str(input())

while len(s)>3:
    print('Введите трехзначное число')
    s = str(input())

if s[0] == s[1] == s[2]:
    print('Число состоит из одинаковых цифр')
else:
    print('Нет')