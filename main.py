# Богушев В.В.
number_of_completed = 12
number_of_hours_spent = 1.5
course_name = 'Python'
time_for_one_task = number_of_hours_spent / number_of_completed
task_ = (f"Курс {course_name}, всего задач:{number_of_completed}, затрачено часов: {number_of_hours_spent}, "
         f"среднее время выполнения {time_for_one_task}")
print(task_)
