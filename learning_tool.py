from question_handler import QuestionHandler
from modes import *
from questions import QuestionModifier

class LearningTool:
     # initialise the question handler, modifier & modes 
    def __init__(self):
        self.question_handler = QuestionHandler()
        self.question_modifier = QuestionModifier(self.question_handler.questions, self.question_handler.disabled_questions)
        self.practice_mode = PracticeMode(self.question_handler)
        self.test_mode = TestMode(self.question_handler)

    def main(self):
        self.question_handler.load_questions() # loads questions from file

        while True:
            print("\n--- Your Learning Tool ---")
            print()
            print("1. Add Questions")
            print("2. View Statistics")
            print("3. Disable/Enable Questions")
            print("4. Practice Mode")
            print("5. Test Mode")
            print()
            print("'q' Exit")
            print()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.question_handler.add_question()
                self.question_handler.save_questions()
            elif choice == "2":
                statistics = Statistics()
                statistics.view_statistics(self.question_handler.questions)
            elif choice == "3":
                sub_choice = input("Do you want to disable or enable a question? (d/e): ")
                if sub_choice.lower() == "d":
                    self.question_modifier.disable_question()
                elif sub_choice.lower() == "e":
                    self.question_modifier.enable_question()
                else:
                    print("Invalid choice.")
            elif choice == "4":
                self.practice_mode.start()
            elif choice == "5":
                self.test_mode.start()
            elif choice == "q":
                break
            else:
                print("Invalid choice. Please try again.")

# create instance of learning tool and run main
if __name__ == "__main__":
    learning_tool = LearningTool()
    learning_tool.main()