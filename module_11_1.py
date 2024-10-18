import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

"""requests - отличная библиотека в две строки позволяет обменятся информацией по HTTP"""
"""pandas - отличная библиотека для быстрой статистической обработки данных"""
"""matplotlib - супер библиотека для быстрого и удобного создания графиков"""

"""Получить диаграммы для сравнения изменений средней результативности в матчах Лиги One по годам"""


def get_data(year) -> list:
    print("запрос")
    result = []
    get_url = f"https://api.sstats.net/games/list?LeagueId=40&Year={year}&format=json&apikey=75kwgw7361l0l1ir"
    response = requests.get(get_url)
    if response.status_code == 200:
        stat = json.loads(response.content)

        for match in stat['data']:
            result.append({'id': match['id'], 'date': match['date'], 'home': match['homeTeam']['name'],
                           'guest': match['awayTeam']['name'], 'homeResult': match['homeResult'],
                           'awayResult': match['awayResult']})
    print("конец запроса")
    return result


if __name__ == '__main__':
    homes = []
    guests = []
    labels = ['2020', '2021', '2022', '2023']
    for cur_year in labels:
        dataFrame = pd.DataFrame(get_data(cur_year))
        try:
            homes.append(dataFrame['homeResult'].mean())
            guests.append(dataFrame['awayResult'].mean())
        except Exception as e:
            print(f"Ошибка получения данных {e}")

    width = 0.35
    fig, ax = plt.subplots()
    ax.bar(labels, homes, width, label='Хозяева')
    ax.bar(labels, guests, width, bottom=homes, label='Гости')
    ax.set_ylabel('Забито голов')
    ax.set_title(f'Среднее количество голов')
    plt.legend(loc='lower left', title='')
    plt.show()
