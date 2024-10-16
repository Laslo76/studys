# Bogushev V.V.
import datetime
from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    if file_name == "":
        raise FileNotFoundError("не задано имя создаваемого файла")
    with open(file_name, 'a', encoding='utf8') as work_file:
        for i in range(word_count):
            print(f'Какое-то слово № {i+1}', file=work_file)
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


start_time = datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
long_time = datetime.now() - start_time
print(f"Работа потоков {long_time}")

start_time = datetime.now()
first_threading = Thread(target=write_words, args=(10, "example5.txt"))
second_threading = Thread(target=write_words, args=(30, "example6.txt"))
third_threading = Thread(target=write_words, args=(200, "example7.txt"))
fourth_threading = Thread(target=write_words, args=(100, "example8.txt"))

first_threading.start()
second_threading.start()
third_threading.start()
fourth_threading.start()

first_threading.join()
second_threading.join()
third_threading.join()
fourth_threading.join()
long_time = datetime.now() - start_time
print(f"Работа потоков {long_time}")
