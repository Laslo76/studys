# Bogushev V.V.

import datetime
import multiprocessing


def read_info(name_file: str):
    all_data = []
    with open(name_file, 'r') as f_:
        str_f = f_.readline()
        while str_f != "":
            str_f = f_.readline()
            all_data.append(str_f)


if __name__ == '__main__':
    name_files = [f'./file {_}.txt' for _ in range(1, 5)]

    # ЛИНЕЙНЫЙ ВЫЗОВ
    start_ = datetime.datetime.now()
    for name in name_files:
        read_info(name)
    end_ = datetime.datetime.now()
    print(f'время линейной работы: {end_ - start_}')

    # МНОГОПРОЦЕССОРНЫЙ ВЫЗОВ
    start_ = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, name_files)
    end_ = datetime.datetime.now()
    print(f'время параллельной работы: {end_ - start_}')
