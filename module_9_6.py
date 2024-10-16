# Bogushev V.V.

def all_variants(text):
    """ Функция генератор проходит заданную строку двумя циклами:
    первый - задает рамку (количество просматриваемых символов)
    второй - пробегает строку выбирая срезы, идем с начала до точки последний нача
    сумма указателя на который плюс размер рамки составляют длину строки
    """
    max_point = len(text) + 1
    for ls in range(1, max_point):
        for point in range(max_point-ls):
            yield text[point:point+ls]


if __name__ == '__main__':
    a = all_variants("abc")
    for i in a:
        print(i)
