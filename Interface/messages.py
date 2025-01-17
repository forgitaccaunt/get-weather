'''
Модуль предназначен для формирования сообщений.

Cодержит шаблоны и функции для создания различных сообщений.
'''

from Settings.config import delay


CITY_TEMPLATE = 'Записываются данные о погоде в г.{} каждые {} минут(ы).'
SUCCESS_TEMPLATE = '{}: успешно.'
ERROR_TEMPLATE = 'Внимание! {}:'
EXIT_TEMPLATE = '\nВыполнение прервано пользователем.'
HELP_TEMPLATE = '''
/show - Вывести данные на экран
/export - Экспортировать данные в .xlsx
/unique_cities - Список городов с данными
/exit - Завершение программы
'''

def city_message(city) -> str:
    # Формирует сообщение о записи данных о погоде для конкретного города.
    return CITY_TEMPLATE.format(city, delay)

def success_message(operation: str) -> str:
    # Формирует сообщение об успешной операции.
    return SUCCESS_TEMPLATE.format(operation)

def error_message(operation, error=None) -> str:
    # Формирует сообщение об ошибке при выполнении операции.
    message = ERROR_TEMPLATE.format(operation)
    if error:
        message += f': {error}.'
    return message

def help_message() -> str:
    # Формирует сообщение с доступными для ввода командами.
    return HELP_TEMPLATE

def exit_message() -> str:
    # Формирует сообщение о завершении программы.
    return EXIT_TEMPLATE

def show_me_weather(last_weather) -> str:
    # Выводит на экран актуальные данные о погоде в текущий момент.
    return f'''
Погода в г.{last_weather.city} на {last_weather.date} в {last_weather.time}:
Температура: {last_weather.temperature}*C
Направление ветра: {last_weather.wind_dir}
Скорость ветра: {last_weather.wind_speed} м/с
Давление: {last_weather.pressure} мм рт. ст.
Осадки: {last_weather.precipitation}, {last_weather.prec_amount} мм
'''
