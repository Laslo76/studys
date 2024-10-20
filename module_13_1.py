import asyncio


async def start_strongman(name: str, loc_power: int):
    if not isinstance(name, str):
        raise TypeError(f"Имя атлета - строка. Получено {type(name)}")
    if not isinstance(loc_power, int):
        raise TypeError(f"Сила атлета - положительное целое число. Получено {type(name)}")
    if loc_power <= 0:
        raise ValueError(f"Сила атлета - положительное целое число. Получено значение {loc_power}")

    print(f"Силач {name} начал соревнования.")
    for number in range(1, 6):
        await asyncio.sleep(5 / loc_power)
        print(f"Силач {name} поднял {number} шар.")
    print(f"Силач {name} закончил соревнования.")


async def main():
    strongmans = {'Pasha': 3, 'Denis': 4,'Apollon': 5}
    tasks = []
    for strongman, power in strongmans.items():
        tasks.append(asyncio.create_task(start_strongman(strongman, power)))

    for task in tasks:
        await task
    
    
if __name__ == '__main__':
    asyncio.run(main())
    