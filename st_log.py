import logging


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        format="%(asctime)s | %(levelname)s | %(message)s",
                        encoding='utf8')
    logging.info("старт")
