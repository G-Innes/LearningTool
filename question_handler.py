import json
from questions import *
from modes import *

# lass to manage question related functionality with methods to load, add & save questions to file
class QuestionHandler:

    file_path = '/Users/grantinnes/Desktop/Dev-Stuff/Turing-College/ginnes-FPCS.3/questions.json'

    def __init__(self):
        self.questions = []
        self.disabled_questions = set()

    # loads questions from JSON file, if no questions found it prompts user to add questions
    def load_questions(self):
        try:
            with open(self.file_path, "r") as file:
                questions_data = json.load(file)

            # iterate over questions_data and extract data into variables
            for question_data in questions_data:
                question_type = question_data["type"]
                question_text = question_data["question_text"]
                answer = question_data["answer"]
                num_shown = question_data.get("num_shown", 0)
                num_correct = question_data.get("num_correct", 0)

                # create Quiz & freeform objects based on question type
                if question_type == "quiz":
                    options = question_data["options"]
                    question = QuizQuestion(question_text, answer, options)
                elif question_type == "freeform":
                    regex_pattern = question_data["regex_pattern"]
                    question = FreeFormQuestion(question_text, answer, regex_pattern)
                else:
                    continue
                # set additional properties for question objects
                # sets default value to 0 if no value is set
                question.num_shown = question_data.get("num_shown", 0)
                question.num_correct = question_data.get("num_correct", 0)
                question.active = True

                # appends objects to questions list
                self.questions.append(question)

        except FileNotFoundError:
            print("No questions found. Start adding questions.")

    # method for adding questions to the self.questions list
    # choose between the 2 types, checks if input is valid & loops if not 
    def add_question(self):
        question_type = input("Enter the type of question (quiz/freeform): ")

        while question_type.lower() not in ["quiz", "freeform"]:
            print("Invalid question type. Choose 'quiz' or 'freeform'")
            question_type = input("Enter the type of question (quiz/freeform): ")

        question_text = input("Enter the question text: ")
        
        # if quiz question, prompts for correct answer & assig ns to variable
        if question_type.lower() == "quiz":
            correct_answer = input("Enter the correct answer: ")
            answers = []
            # loops for answer options until 'q' is entered (must include the correct answer again)
            # appends each option to the answers list
            while True:
                option = input("Enter an answer option & include correct answer('q' to exit): ")
                if option.lower() == "q":
                    break
                answers.append(option)
            # creates question as QuizQuestion object and appends to self.questions list
            self.questions.append(QuizQuestion(question_text, correct_answer, answers))

        # if freeform question, user is prompted for answer and the regex pattern for matching
        elif question_type.lower() == "freeform":
            answer = input("Enter the answer: ")
            regex_pattern = input("Enter the regex pattern for the answer: ")
            # creates question as FreeformQuestion object and appends to list
            self.questions.append(FreeFormQuestion(question_text, answer, regex_pattern))

        print("Question added successfully!")

    # method for saving questions in 'self.questions' list to JSON file
    def save_questions(self):
        questions_data = [] # empty list for storing question data dicts

        # iterate over self.questions tracking index with enumerate
        # creates question data dictionary for each question storing required key value pairs
        for index, question in enumerate(self.questions):
            question_data = {
                "ID": index + 1,
                "type": "quiz" if isinstance(question, QuizQuestion) else "freeform",
                "question_text": question.question_text,
                "answer": question.answer,
                "num_shown": question.num_shown,
                "num_correct": question.num_correct
            }
            # adds answer options for quiz type question
            if isinstance(question, QuizQuestion):
                question_data["options"] = question.options
            # adds regex patter for freeform question
            elif isinstance(question, FreeFormQuestion):
                question_data["regex_pattern"] = question.regex_pattern
            # append question data dictionary to questions data list
            questions_data.append(question_data)
        # writes list to JSON file
        with open(self.file_path, "w") as file:
            json.dump(questions_data, file, indent=4)