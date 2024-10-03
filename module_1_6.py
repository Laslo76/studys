# Богушев В.В.
# dict
my_dict = {'admin': 'Sdx34%21', 'user': '&hdbfdsyrwl3s'}

print(my_dict)
print(my_dict["admin"])
print(my_dict.get("Ivan", 'Неизвестный пользователь'))

my_dict.update({"Ivan": 'yudfh^3hjxc', 'Gerasim': 'BNEHDF7hJHDF6Y#'})
print(my_dict)

my_pass = my_dict.pop("user")
print(my_pass)

print(my_dict)

#set
my_set = {3, 'Саратов', 3.0, 2, 3} # Любопытно, что цело 3 и вещественное 3.0 считаются тождественными
print(my_set)
my_set.add((123, 56.456456))
my_set.add(3.14)

print(my_set)

my_set.discard('Саратов')
print(my_set)
