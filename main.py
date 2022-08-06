from sqlalchemy.orm import declarative_base
from sqlalchemy import column, string, dateTime, Integer, create_engine
from datetime import datetime
import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///" + os.path.join(BASE_DIR, 'palabras.db')

Base = declarative_base()

engine = create_engine(connection_string, echo = True)

""""
class Dictionary
    id int
    word str
    meaning str

    date_created datetime

"""

class Word(Base):
    __tableName__ = 'Diccionario'
    id = column(Integer(), primary_key = True)
    word = column(String(25),nullable = False,unique = True)
    meaning = (String(90),nullable = False, unique = False)
    date_created = column(dateTime(),default = datetime.utcnow)

    def __repr__(self):
        return f"<Word word = {self.word} meaning = {self.meaning}"

new_word = Word(id=1, word="", meaning="")