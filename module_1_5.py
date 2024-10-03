# Богушев В.В.
immutable_var = ('First', 1, ['Bogushev', 'Vladislav'])
print(immutable_var)

try:
    immutable_var[0] = 'Second'
except:
    print("Изменить кортеж нельзя")

print(immutable_var[0])

# Но можно изменить изменяемый элемент кортежа
immutable_var[2][1] = 'Vlad'
print(immutable_var)
