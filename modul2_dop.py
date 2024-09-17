# Bogushev V.V.

while True:
    key_number = int(input("Введите число от 3 до 20: "))
    if (key_number > 2) and (key_number < 21):
        break
    else:
         print("Неверно введено число! Повторите попытку!")

str_resault = ""
first = 1
while first < key_number:
    second = first + 1
    while second < key_number:
         if key_number % (first + second) == 0:
              str_resault += str(first) + str(second)
         second += 1
    first += 1
print(f'{key_number} - {str_resault}')
