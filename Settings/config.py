"""
Конфигурационный файл проекта.

Этот модуль содержит пути к базам данных, словари данных и глобальные переменные.
"""

# Путь к базе данных
db_path = '/content/drive/My Drive/ColabNotebooks/gwth/files/weather_db.db'
# Путь к файлу .xlsx
xlsx_path = '/content/drive/My Drive/ColabNotebooks/gwth/files/weather.xlsx'

# Конфигурация базы данных
sqlite_database = "sqlite:///" + db_path

# Словарь для хранения городов в виде Город: Широта, Долгота
cities = {
        "Москва": (55.751244, 37.618423),
        "Санкт-Петербург": (59.9342802, 30.3350986)
}

# Инициализация розы ветров
rose = range(0, 361, 45)
wind = ['С', 'СВ', 'В', 'ЮВ', 'Ю', 'ЮЗ', 'З', 'СЗ', 'С']
wind_rose = dict(zip(rose, wind))

# Словарь, который содержит различные типы осадков
precipitation_map = {
    'rain': ('Дождь', 'rain'),
    'showers': ('Ливень', 'showers'),
    'snowfall': ('Снегопад', 'snowfall')
}

# Интервал получения данных о погоде (в минутах)
delay = 0.1
# Ограничение на количество строк для экспорта в файлы
rows = 10
