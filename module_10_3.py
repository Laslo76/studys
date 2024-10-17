from threading import Thread, Lock
from time import sleep
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            sum_add = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += sum_add
            print(f'Пополнение: {sum_add}. Баланс: {self.balance}.')
            sleep(0.001)

    def take(self):
        for i in range(100):
            sum_sub = randint(50, 500)
            print(f'Запрос на {sum_sub}')
            if self.balance >= sum_sub:
                self.balance -= sum_sub
                print(f'Снятие: {sum_sub}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


if __name__ == '__main__':
    bank = Bank()

    making = Thread(target=Bank.deposit, args=(bank,))
    withdrawals = Thread(target=Bank.take, args=(bank,))

    making.start()
    withdrawals.start()

    making.join()
    withdrawals.join()

    print(f"Итоговый баланс: {bank.balance}")
