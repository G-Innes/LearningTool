import re

# represents a generic question with its text, answer,
# active status, number of times shown, and number of correct answers.
class Question:
    def __init__(self, question_text, answer):
        self.question_text = question_text
        self.answer = answer
        self.active = True
        self.num_shown = 0
        self.num_correct = 0

# inherits from Question and adds list of options
class QuizQuestion(Question):
    def __init__(self, question_text, answer, options):
        super().__init__(question_text, answer)
        self.options = options

    # compares user answer with correct answer & returns true if match
    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()
    
# inherits from Question and adds the regex pattern
class FreeFormQuestion(Question):
    def __init__(self, question_text, answer, regex_pattern):
        super().__init__(question_text, answer)
        self.regex_pattern = regex_pattern

    # checks if user answer matches regex pattern
    def check_answer(self, user_answer):
        return re.match(self.regex_pattern, user_answer)
    
# class to hande enable/disable of questions
class QuestionModifier:
    def __init__(self, questions, disabled_questions):
        self.questions = questions
        self.disabled_questions = disabled_questions

    # prompts user to enter ID of question retrieves question from questions list -1 so indexing matches ID
    def disable_question(self):
        try:
            question_id = int(input("Enter the ID of the question to disable: "))
            question = self.questions[question_id - 1]
        except (ValueError, IndexError):
            print("Incorrect entry type. Must be an integer within questions index")
            return
        
        # prints details of question selected & prompts for confirmation & sets active status to false, adds to disabled questions list
        print("Question Details:")
        print(f"Question Text: {question.question_text}")
        print(f"Answer: {question.answer}")
        confirmation = input("Are you sure you want to disable this question? (y/n): ")
        if confirmation.lower() == "y":
            question.active = False
            self.disabled_questions.add(question_id - 1)
            print("Question disabled successfully!")
        else:
            print("No action taken")

    def enable_question(self):
        try:
            question_id = int(input("Enter the ID of the question to enable: "))
            question = self.questions[question_id - 1]
        except (ValueError, IndexError):
            print("Incorrect entry type. Must be an integer within questions index")
            return
        print("Question Details:")
        print(f"Question Text: {question.question_text}")
        print(f"Answer: {question.answer}")
        # prints details of question selected & prompts for confirmation & sets active status to true, removes from disabled questions list
        confirmation = input("Are you sure you want to enable this question? (y/n): ")
        if confirmation.lower() == "y":
            try:
                question.active = True
                self.disabled_questions.remove(question_id - 1)
                print("Question enabled successfully!")
            except KeyError:
                print("Question already active")
                return
        else:
            print("No action taken")