import logging
import unittest
import rt_with_exceptions as cls_runner

logging.basicConfig(level=logging.DEBUG, filemode='w', filename='runner_tests.log',
                    format="%(asctime)s | %(levelname)s | %(message)s",
                    encoding='utf8', force=True)


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            data = ['Michel', 2]
            test_one = cls_runner.Runner(*data)
        except TypeError as er:
            logging.error(f"Ошибка создания бегуна. {er}.")
        except ValueError as er:
            logging.error(f"Ошибка создания бегуна. {er}.")
        else:
            logging.info(f"Создан бегун {data[0]}. Его скорость {data[1]}")
            for i in range(10):
                test_one.walk()
            self.assertEqual(test_one.distance, test_one.speed * 10)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            data = ['Scotti', 5]
            test_one = cls_runner.Runner(*data)
        except TypeError as er:
            logging.error(f"Неверный тип данных для объекта Runner. {er}.")
        except ValueError as er:
            logging.error(f"Неверная скорость для Runner. {er}.")
        else:
            logging.info(f"Создан бегун {data[0]}. Его скорость {data[1]}")
            for i in range(10):
                test_one.walk()
            self.assertEqual(test_one.distance, test_one.speed * 10)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        names = ['Jan', 0, True]
        speeds = [-3, 0, 5]
        runners = []
        for data in zip(names, speeds):
            try:
                runners.append(cls_runner.Runner(*data))
            except TypeError as er:
                logging.error(f"Неверный тип данных для объекта Runner. {er}.")
            except ValueError as er:
                logging.error(f"Неверная скорость для Runner. {er}.")
            else:
                logging.info(f"Создан бегун {data[0]}. Его скорость {data[1]}")

            for runner in runners:
                for i in range(10):
                    runner.walk()
                    runner.run()
                self.assertEqual(runner.distance, runner.speed * 30)


if __name__ == '__main__':
    unittest.main()
