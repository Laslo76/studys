from fake_math import divide as f_div
from true_math import divide as t_div


result1 = f_div(67, 3)
result2 = f_div(3, 0)
result3 = t_div(49, 7)
result4 = t_div(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)
