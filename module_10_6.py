import multiprocessing
import datetime


def worker(data):
    result = data ** 2
    return result


if __name__ == '__main__':

    data = [x for x in range(1, 1_500_001)]
    start_ = datetime.datetime.now()
    result = list(map(worker, data))
    stop_ = datetime.datetime.now()
    print(f'время обычное - {stop_ - start_}')
    #print(result)

    data = [x for x in range(1, 1_500_001)]
    start_ = datetime.datetime.now()

    pool = multiprocessing.Pool(processes=2)
    #result = pool.map(worker, data)

    pool.close()
    pool.join()

    stop_ = datetime.datetime.now()
    print(f'время мультипроцессорное - {stop_ - start_}')
    #print(result)
