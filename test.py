import pytest
from questions import *
from question_handler import *
from modes import *
from learning_tool import *


# Unit test for the QuizQuestion class
def test_quiz_question_check_answer():
    
    options = ["Reptile", "Mammal", "Fish", "Bird"]
    question = QuizQuestion("What is a Python?", "Reptile", options)

    result = question.check_answer("Reptile")

    assert result == True

def test_quiz_question_check_answer_case_insensitive():
    
    options = ["reptile", "mammal", "fish", "bird"]
    question = QuizQuestion("What is a Python?", "Reptile", options)

    result = question.check_answer("reptile")

    assert result == True


# Unit tests for the QuestionHandler class
def test_question_handler_load_questions():
    
    question_handler = QuestionHandler()

    question_handler.load_questions()

    assert len(question_handler.questions) > 0

def test_question_handler_save_questions(tmp_path):
    
    question_handler = QuestionHandler()
    question_handler.questions.append(Question("Question 1", "Answer 1"))
    question_handler.questions.append(Question("Question 2", "Answer 2"))

    file_path = tmp_path / "questions.json"
    question_handler.file_path = file_path
    question_handler.save_questions()

    assert file_path.exists()

