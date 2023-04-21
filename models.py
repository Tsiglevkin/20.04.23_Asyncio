from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sq

from dotenv import dotenv_values
secrets_value = dotenv_values('.env')

USER = secrets_value['USER']
PASSWORD = secrets_value['PASSWORD']
HOST = secrets_value['HOST']
PORT = secrets_value['PORT']
DB_NAME = secrets_value['DB_NAME']

DSN = f'postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'

engine = create_async_engine(DSN)
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


class SwapiPeople(Base):
    __tablename__ = 'people'

    person_id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    birth_year = sq.Column(sq.Date)
    eye_color = sq.Column(sq.String(50))
    films = sq.Column(sq.String(200))
    gender = sq.Column(sq.String(50))
    hair_color = sq.Column(sq.String(50))
    height = sq.Column(sq.Integer)
    homeworld = sq.Column(sq.String(50))
    mass = sq.Column(sq.Integer)
    name = sq.Column(sq.String(50))
    skin_color = sq.Column(sq.String(50))
    species = sq.Column(sq.String(200))
    starships = sq.Column(sq.String(200))
    vehicles = sq.Column(sq.String(200))


def prepare_to_orm(some_json: dict):
    for key, value in some_json.items():
        if type(value) == list:
            some_json[key] = (', '.join(value))
    return some_json


async def paste_people(people_json_list):
    for some_json in people_json_list:
        prepare_to_orm(some_json)

    async with Session() as session:
        orm_people = [SwapiPeople(**person_json) for person_json in people_json_list]
        session.add_all(orm_people)
        await session.commit()



