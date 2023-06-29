import time
from prnewswire import one_cicle as one_cicle_prnewswire

def main(period = 2, work_time_in_minute = 7):
    """Запускает программу на определенный период

    Args:
        period (int, optional): период в секундах, для простоя парсинга между двумя сессиями (2 секунды)
        work_time_in_minute (int, optional): время в минутах работы программы (7 минут)

    """
    #проверка корректности аргументов
    if work_time_in_minute > 15 or work_time_in_minute < 0.1:
        return 'false work time'
    all_time = work_time_in_minute * 60 #время работы в секундах
    #слишком большой или слишкой малый периоды
    if period > 70 or period < 1:
        return 'false time period'
    count = int(all_time / period) #кол-во запусканий
    print(count)
    #запуск работы метода
    for i in range(count): 
        one_cicle_prnewswire()
        time.sleep(period)
    
main(work_time_in_minute=0.1)