"""Описать таблицы из lesson12/homework.sql при помощи sqlalchemy"""
from sqlalchemy import (
    create_engine,
    MetaData,
    Column,
    Integer,
    String)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'postgres://postgres:postgres@localhost:5432/sqlalchemy'
)
metadata = MetaData()

BaseModel = declarative_base(bind=engine)

class User_name(BaseModel):
    __tablename__ = 'User_name'

    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)

    def __repr__(self):
        return f"id = {self.id}, name = {self.name}"

class Tests(BaseModel):
    __tablename__ = 'Tests'

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    text = Column(String, nullable=False)

    def __repr__(self):
        return f"id = {self.id}, number = {self.number}, text = {self.text}"

class Questions(BaseModel):
    __tablename__ = 'Questions'

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    text = Column(String, nullable=False)

    def __repr__(self):
        return f"id = {self.id}, number = {self.number}, text = {self.text}"


class Test_Questions(BaseModel):
    __tablename__ = 'Test_questions'

    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, nullable=False, unique=True)
    question_id = Column(Integer, nullable=False, unique=True)

    def __repr__(self):
        return f"id = {self.id}, test_id = {self.test_id}, question_id = {self.question_id}"

class Answers(BaseModel):
    __tablename__ = 'Answers'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    is_correct = Column(Boolean, default=False)
    id_question = Column(Integer, ForeignKey('question.id'))

    def __repr__(self):
        return f"id = {self.id}, text = {self.text}, is_correct = {self.is_correct}, id_question = {self.id_questiond}"

class Users_answers(BaseModel):
    __tablename__ = 'Users_answers'

    id = Column(Integer, primaty_key=True)
    tests_questions_id = Column(Integer, ForeignKey('test_questions.id'), unique = True)
    user_id = Column(Integer, ForeignKey('username.id'), unique = True)
    answer_id = Column(Integer, ForeignKey('answers.id'))

    def __repr__(self):
        return f"id = {self.id}, tests_questions_id = {self.tests_questions_id}, user_id = {self.user_id}, answer_id = {self.answer_id}"

BaseModel.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()








