from person import Person
from fastapi import FastAPI
from pydantic import BaseModel
from model_utils import load_model, predict_prod

class Database:
    def __init__(self) -> None:
        self.__d = dict()
        self.__internal_index = 0

    def create(self, record: Person) -> int:
        current_index = self.__internal_index
        self.__d[current_index] = record
        self.__internal_index += 1
        return current_index

    def update(self, index, record: Person):
        self.__d[index] = record

    def read(self, index: int) -> Person:
        return self.__d[index]

    def delete(self, index):
        del self.__d[index]

    def list_records(self) -> list[Person]:
        return list(self.__d.values())


