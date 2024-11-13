# Импорт зависимостей
from Setting.config import xlsx_path, rows
from base import WeatherData, Weather, Base
# Импорт библиотек
import pandas as pd
from typing import Generator
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from contextlib import contextmanager


class DataBaseManager :
    '''
    Класс-менеджер для управления данными в контексте БД.
    Используется @contextmanager для безопасных сессий.
    '''
    def __init__(self, sqlite_database):
        self.engine = create_engine(sqlite_database, echo=False)
        Base.metadata.create_all(self.engine)

    @contextmanager
    def session_scope(self) -> Generator[Session, None, None]:
        # Контекстный менеджер для управления сессиями
        session = Session(self.engine)
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()  # Откатываем изменения в случае ошибки
            raise e
        finally:
            session.close()

    async def save_weather(self, weather: Weather):
        # Запись полученных данных о погоде в БД
        async with self.session_scope() as session:
            new_record = WeatherData(
                city=weather.city,
                date=weather.date,
                time=weather.time,
                temperature=weather.temperature,
                wind_dir=weather.wind_dir,
                wind_speed=weather.wind_speed,
                pressure=weather.pressure,
                precipitation=weather.precipitation,
                prec_amount=weather.prec_amount
            )
            session.add(new_record)
        print('Данные успешно сохранены в БД')

    async def get_last_weather(self):
        # Извлечение последней записи из БД
        async with self.session_scope() as session:
            weather_data = session.query(WeatherData).order_by(WeatherData.id.desc()).first()
            
            if weather_data:
                return Weather(
                    city=weather_data.city,
                    date=weather_data.date,
                    time=weather_data.time,
                    temperature=weather_data.temperature,
                    wind_dir=weather_data.wind_dir,
                    wind_speed=weather_data.wind_speed,
                    pressure=weather_data.pressure,
                    precipitation=weather_data.precipitation,
                    prec_amount=weather_data.prec_amount
                )
            else:
                raise ValueError("No weather data available.")

    async def export_to_xlsx(self):
        # Экспорт последней записи из БД в файл xlsx
        async with self.session_scope() as session:
            query = session.query(WeatherData).order_by(WeatherData.id.desc()).limit(rows)
            df = pd.read_sql_query(query.statement, con=self.engine)
            async with pd.ExcelWriter(xlsx_path, mode='w') as writer:
                df.to_excel(writer, index=False, sheet_name='Sheet_1')
            print('Данные экспортированы\n')