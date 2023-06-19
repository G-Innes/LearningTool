from questions import *
import random
import datetime


class Statistics:

    # takes list of questions and displays stats for each question
    def view_statistics(self, questions):
        print()
        print("-"*25)
        print("Question Statistics:")
        print()
        # iterates over each question in list, printing the selected data
        for i, question in enumerate(questions):
            print(f"Question ID: {i + 1}")
            print(f"Active: {'Yes' if question.active else 'No'}")
            print(f"Question Text: {question.question_text}")
            print(f"Times Shown: {question.num_shown}")
            percentage = question.num_correct / question.num_shown * 100 if question.num_shown > 0 else 0
            print(f"Percentage Correct: {percentage}%")
            print("-"*25)
            print()

class PracticeMode:
    def __init__(self, question_handler):
        self.question_handler = question_handler

    # if not enough questions, prints message and returns
    def start(self):
        if len(self.question_handler.questions) < 5:
            print("At least 5 questions are required to enter practice mode.")
            return

        # loops through questions at random & breaks when user does not enter 'y' when prompted 
        while True:
            # randomely selects questions from question_handler_questions list, assigns weights of 1 if not in disabled q's list
            # ensures that questions that are disabled are not selected as weighted with 0
            weights = [1 if i not in self.question_handler.disabled_questions else 0 for i in range(len(self.question_handler.questions))]
            question = random.choices(self.question_handler.questions, weights=weights)[0]

            # if question is active, checks if instance of quiz question & gives answer options enumerating them
            if question.active:
                if isinstance(question, QuizQuestion):
                    print(question.question_text)
                    for i, option in enumerate(question.options):
                        print(f"{i + 1}. {option}")
                    while True:
                        try:
                            user_answer = input("Enter the option number: ")
                            user_answer = question.options[int(user_answer) - 1] # subtracts 1 from user input to align with indexing
                            break
                        except (ValueError, IndexError):
                            print('Invalid option (expected: integer within answers index)')
                else: 
                    user_answer = input(question.question_text + ": ") # if not instance of quiz then reverts to freeform

                # calls check_answer method and increments num_correct if True is returned, otherwise only num_shown is incremented 
                if question.check_answer(user_answer):
                    print()
                    print("🎉 Correct answer! 🎉")
                    print()
                    question.num_correct += 1
                else:
                    print()
                    print("Incorrect answer! 👎🏻")
                    print()
                question.num_shown += 1

                continue_practice = input("Continue practicing? (y/n): ")
                if continue_practice.lower() != "y":
                    break

class TestMode:
    test_results = '/Users/grantinnes/Desktop/Dev-Stuff/Turing-College/ginnes-FPCS.3/results.txt'

    def __init__(self, question_handler):
        self.question_handler = question_handler
        self.results = []

    def start(self):
        if len(self.question_handler.questions) < 5:
            print("At least 5 questions are required to enter test mode.")
            return

        num_questions = int(input("Enter the number of questions for the test: "))
        if num_questions > len(self.question_handler.questions):
            print("Not enough questions available.")
            return

        # randomly selects the number of questions from the list & assigns to test_questions
        test_questions = random.sample(self.question_handler.questions, num_questions)
        score = 0

        for question in test_questions:
            if isinstance(question, QuizQuestion):
                print(question.question_text)
                for i, option in enumerate(question.options):
                    print(f"{i + 1}. {option}")
                while True:
                    try:
                        user_answer = input("Enter the option number: ")
                        user_answer = question.options[int(user_answer) - 1]
                        break
                    except (ValueError, IndexError):
                        print('Invalid option (expected: integer within answers index)')
            else:
                user_answer = input(question.question_text + ": ")

            if question.check_answer(user_answer):
                print()
                print("🎉 Correct answer! 🎉")
                print()
                score += 1
                question.num_correct += 1
                self.results.append("Correct")  # store result as correct 
                
            else:
                print()
                print("Incorrect answer! 👎🏻")
                print()
                self.results.append("Incorrect ")  # store result as incorrect
            question.num_shown += 1
        self.save_results(score, num_questions, test_questions) # calls method with relevant parameters

        print(f"Test score: {score}/{num_questions}")

    # method to take results of the text and save to results.txt file with timestamp, questions and whether user got crooect or not 
    def save_results(self, score, num_questions, questions):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result_string = f"Score: {score}/{num_questions} - {timestamp}\n\n"
        question_results = []

        for i , result in enumerate(self.results):
            question_result = f"{i+1}. {questions[i].question_text}: {result}\n"
            question_results.append(question_result)

        result_string += "\n".join(question_results)

        with open(self.test_results, "a") as file:
            file.write(result_string)

            # Bug fix- 19/6/23: question text not being added correctly to results.txt
            # edited argument in method call, ammended loop to access each question text
