# Bogushev V.V.
# formatting strings

def num_postfix(num: int, word: str) -> str:
    if word.lower() == 'участник':
        rest_ = num % 10
        nast_ = num // 10
        if rest_ == 1 and nast_ != 1:
            return word
        elif rest_ in range(2, 5) and nast_ != 1:
            return word+'а'
        else:
            return word+'ов'
    elif word.lower() == 'задача':
        rest_ = num % 10
        nast_ = num // 10
        if rest_ == 1 and nast_ != 1:
            return 'задачу'
        elif rest_ in range(2, 5) and nast_ != 1:
            return 'задачи'
        else:
            return 'задач'


if __name__ == "__main__":
    team1_name = "Мастера кода"
    team2_name = "Волшебники данных"
    team1_num = 5
    team2_num = 6
    score_1 = 40
    score_2 = 42
    team1_time = 1552.512
    team2_time = 2153.31451

    tasks_total = score_1 + score_2
    time_avg = (team1_time + team1_time) / tasks_total
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        challenge_result = f"победа команды {team1_name}"
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        challenge_result = f"победа команды {team2_name}"
    else:
        "ничья"

    print("В команде Мастера кода %s: %d !" % (num_postfix(team1_num, "участник"), team1_num))
    print("Итого сегодня в обеих командах %s: %d и %d" % (num_postfix(team2_num, "участник"),
                                                          team1_num, team2_num))

    print("Команда Волшебники данных решила {} {}".format(score_2, num_postfix(score_2, "задача")))
    print("Волшебники данных решили {} за {} с !".format(num_postfix(score_2, "задача"), team2_time))

    print(f"Команды решили {score_1} и {score_2} {num_postfix(score_2, 'задача')}.")
    print(f"Результат битвы: {challenge_result}!")
    print(f"Сегодня было решено {tasks_total} {num_postfix(tasks_total, "задача")},\n"
          f" в среднем по  {time_avg} секунды на задачу!")
